#include "ant.h"

#include <sstream>

#include <plog/Log.h>

namespace ant_colony {

Ant::Ant(World &world, int id)
    : id_(id), state_(Ant::State::LOOKING_FOR_FOOD), world_(world) {
  location_ = world_.getHomeBase();
  foodList_.clear();

  PLOG_VERBOSE << "Ant() with id " << id_ << " created!";
}

Location Ant::getLocation() const { return location_; }

void Ant::step() {
  if (state_ == State::LOOKING_FOR_FOOD) {
    // Deal with the food location first
    if (knowsFoodLocations()) {
      PLOG_VERBOSE << "Ant " << id_ << " is at " << location_.toString()
                   << " and is moving towards "
                   << getNextFoodLocation().toString();
      moveTowards(getNextFoodLocation());
    } else {
      PLOG_VERBOSE << "Ant " << id_ << " is at " << location_.toString()
                   << " and is moving randomly.";
      moveRandom();
    }

    // Always try to get food, maybe there are some new sources on the way
    if (tryToGrabFood()) {
      if (location_ == getNextFoodLocation()) {
        PLOG_DEBUG << "Ant " << id_
                   << " picked up food from known food location "
                   << location_.toString() << "!";
      } else {
        foodList_.insert(location_);

        PLOG_INFO << "Ant " << id_ << " found a new food location at "
                  << location_.toString();
        getFoodListAsStr();
      }

      state_ = State::RETURNING_HOME;
    } else {
      if (knowsFoodLocations() && (location_ == getNextFoodLocation())) {
        // Here should be food, but nothing found
        // --> Delete location from foodList_!
        foodList_.erase(location_);
        PLOG_DEBUG << "Ant " << id_ << " erased location "
                   << location_.toString() << " from foodList_!";
        getFoodListAsStr();
      }
    }

  } else if (state_ == State::RETURNING_HOME) {
    // Return home to deliver food!
    moveTowards(world_.getHomeBase());
    if (deliverFood()) {
      state_ = State::LOOKING_FOR_FOOD;
      PLOG_DEBUG << "Ant " << id_ << " delivered food at home base "
                 << world_.getHomeBase().toString();
    }
  }

  // Always ask potential neighbors for more food locations!
  askForFood();

  // printPosition();
}

void Ant::move(const MovingDirection moving_direction) {
  switch (moving_direction) {
  case MovingDirection::RIGHT:
    if (location_.x < world_.getXDimension() - 1) {
      PLOG_VERBOSE << "Moving RIGHT!";
      location_.x += 1;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::UP:
    if (location_.y < world_.getYDimension() - 1) {
      PLOG_VERBOSE << "Moving UP!";
      location_.y += 1;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::LEFT:
    if (location_.x > 0) {
      PLOG_VERBOSE << "Moving LEFT!";
      location_.x -= 1;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::DOWN:
    if (location_.y > 0) {
      PLOG_VERBOSE << "Moving DOWN!";
      location_.y -= 1;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  default:
    PLOG_ERROR << "Unexpected moving direction for moving of Ant! "
               << static_cast<int>(moving_direction);
  }
}

void Ant::moveTowards(const Location &destination) {
  if (location_.x > destination.x) {
    move(MovingDirection::LEFT);
  } else if (location_.x < destination.x) {
    move(MovingDirection::RIGHT);
  }

  if (location_.y < destination.y) {
    move(MovingDirection::UP);
  } else if (location_.y > destination.y) {
    move(MovingDirection::DOWN);
  }

  PLOG_VERBOSE << "It\'s now at " << location_.toString();
}

void Ant::moveRandom() {
  int r = rand() % static_cast<int>(MovingDirection::MOVING_DIRECTION_SIZE);
  move(static_cast<MovingDirection>(r));
}

bool Ant::tryToGrabFood() {
  if (world_.takeFoodFrom(location_)) {
    return true;
  } else {
    return false;
  }
}

void Ant::askForFood() {
  auto neighborAnts = world_.ant_colony_.getAntsAt(location_);
  for (const auto &other_ant : neighborAnts) {
    if ((other_ant->getId() != id_) && other_ant->knowsFoodLocations() &&
        other_ant->getFoodList() != foodList_) {
      for (const auto &food_location : other_ant->getFoodList()) {
        foodList_.insert(food_location);
      }
      PLOG_DEBUG << "Ant " << id_ << " got food locations from Ant "
                 << other_ant->getId() << ": " << getFoodListAsStr();
    }
  }
}

bool Ant::knowsFoodLocations() const { return (foodList_.size() > 0); }

bool Ant::deliverFood() {
  if (location_ == world_.getHomeBase()) {
    world_.deliverFoodAtHomeBase();
    return true;
  } else {
    return false;
  }
}

std::set<Location> Ant::getFoodList() const { return foodList_; }

Location Ant::getNextFoodLocation() const { return *foodList_.cbegin(); }

Ant::State Ant::getState() const { return state_; }

int Ant::getId() const { return id_; }

string_view Ant::getType() const { return "Ant"; }

string Ant::getFoodListAsStr() const {
  stringstream ss;
  ss << " foodList_: [ ";
  for (const auto &food_location : foodList_) {
    ss << food_location.toString() << ", ";
  }
  ss << " ]";
  return ss.str().c_str();
}

QuickAnt::QuickAnt(World &world, int id) : Ant(world, id), step_size_(2) {
  PLOG_VERBOSE << "QuickAnt() with id " << id_ << " created!";
}

void QuickAnt::move(const MovingDirection moving_direction) {
  switch (moving_direction) {
  case MovingDirection::RIGHT:
    if (location_.x < world_.getXDimension() - step_size_) {
      PLOG_VERBOSE << "Moving RIGHT!";
      location_.x += step_size_;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::UP:
    if (location_.y < world_.getYDimension() - step_size_) {
      PLOG_VERBOSE << "Moving UP!";
      location_.y += step_size_;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::LEFT:
    if (location_.x - step_size_ > 0) {
      PLOG_VERBOSE << "Moving LEFT!";
      location_.x -= step_size_;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  case MovingDirection::DOWN:
    if (location_.y - step_size_ > 0) {
      PLOG_VERBOSE << "Moving DOWN!";
      location_.y -= step_size_;
    } else {
      PLOG_VERBOSE << "Cannot move there, would fall off the world otherwise.";
    }
    break;
  default:
    PLOG_ERROR << "Unexpected moving direction for moving of Ant! "
               << static_cast<int>(moving_direction);
  }
}

string_view QuickAnt::getType() const { return "QuickAnt"; }

} // namespace ant_colony
