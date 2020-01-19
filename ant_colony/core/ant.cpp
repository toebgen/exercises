#include "ant.h"

#include <sstream>

namespace ant_colony {

Ant::Ant(World& world, int id) :
  id_(id),
  state_(Ant::State::LOOKING_FOR_FOOD),
  world_(world)
  {
    location_ = world_.getHomeBase();
    foodList_.clear();
  }

Location Ant::getLocation() const {
  return location_;
}

void Ant::step() {
  if (state_ == State::LOOKING_FOR_FOOD){
    // Deal with the food location first
    if (knowsFoodLocations()) {
      moveTowards(getNextFoodLocation());
    } else {
      moveRandom();
    }

    // Always try to get food, maybe there are some new sources on the way
    if (tryToGrabFood()){
      if (location_ == getNextFoodLocation()){
        printf("Ant %d picked up food from known food location %s!\n",
          id_, location_.toString().c_str());
      } else {
        foodList_.insert(location_);
        
        printf("Ant %d found a new food location at %s! ",
          id_, location_.toString().c_str());
        printFoodList();
      }

      state_ = State::RETURNING_HOME;
    } else {
      if (knowsFoodLocations() && (location_ == getNextFoodLocation())) {
        // Here should be food, but nothing found
        // --> Delete location from foodList_!
        foodList_.erase(location_);
        printf("Ant %d erased location %s from foodList_! ",
          id_, location_.toString().c_str());
        printFoodList();
      }
    }

  } else if (state_ == State::RETURNING_HOME) {
    // Return home to deliver food!
    moveTowards(world_.getHomeBase());
    if (deliverFood()) {
      state_ = State::LOOKING_FOR_FOOD;
      printf("Ant %d delivered food at home base %s\n",
        id_, world_.getHomeBase().toString().c_str());
    }
  }

  // Always ask potential neighbors for more food locations!
  askForFood();

  //printPosition();
}

void Ant::move(const MovingDirection moving_direction) {
  switch(moving_direction) {
    case MovingDirection::RIGHT:
      if (location_.x < world_.getXDimension()-1) location_.x += 1;
      break;
    case MovingDirection::UP:
      if (location_.y < world_.getYDimension()-1) location_.y += 1;
      break;
    case MovingDirection::LEFT:
      if (location_.x > 0) location_.x -= 1;
      break;
    case MovingDirection::DOWN:
      if (location_.y > 0) location_.y -= 1;
      break;
    default:
      printf("Unexpected moving direction for moving of Ant! %d\n",
        moving_direction);
  }
}

void Ant::moveTowards(const Location& destination) {
  // printf("Ant %d is at %s, moving towards %s. ",
  //   id_, location_.toString().c_str(), destination.toString().c_str());
  
  if (location_.x > destination.x) {
    move(MovingDirection::LEFT);
    // printf("Moving LEFT! ");
  } else if (location_.x < destination.x) {
    move(MovingDirection::RIGHT);
    // printf("Moving RIGHT! ");
  }

  if (location_.y < destination.y) {
    move(MovingDirection::UP);
    // printf("Moving UP! ");
  } else if (location_.y > destination.y) {
    move(MovingDirection::DOWN);
    // printf("Moving DOWN! ");
  }

  // printf("It\'s now at %s.\n", location_.toString().c_str());
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
  for (const auto& other_ant : neighborAnts) {
    if ((other_ant->getId() != id_) && other_ant->knowsFoodLocations()
      && other_ant->getFoodList() != foodList_) {
      for (const auto& food_location : other_ant->getFoodList()) {
        foodList_.insert(food_location);
      }
      printf("Ant %d got food locations from Ant %d. ",
        id_, other_ant->getId());
      printFoodList();
    }
  }
}

bool Ant::knowsFoodLocations() const {
  return (foodList_.size() > 0);
}

bool Ant::deliverFood() {
  if (location_ == world_.getHomeBase()){
    world_.deliverFoodAtHomeBase();
    return true;
  } else {
    return false;
  }
}

std::set<Location> Ant::getFoodList() const {
  return foodList_;
}

Location Ant::getNextFoodLocation() const {
  return *foodList_.cbegin();
}

Ant::State Ant::getState() const {
  return state_;
}

int Ant::getId() const {
  return id_;
}

void Ant::printPosition() const {
  printf("Ant %d is at position %s\n", id_, location_.toString().c_str());
}

void Ant::printFoodList() const {
  stringstream ss;
  ss << " foodList_: [ ";
  for (const auto& food_location : foodList_) {
    ss << food_location.toString() << ", ";
  }
  ss << " ]" << endl;

  printf("%s", ss.str().c_str());
}

}  // namespace ant_colony
