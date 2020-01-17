#include "ant.h"

namespace ant_colony {

Ant::Ant(World& world, int id) :
  world_(world),
  id_(id),
  state_(Ant::State::LOOKING_FOR_FOOD)
  {
    location_ = world_.getHomeBase();
  }

Location Ant::getLocation() const {
  return location_;
}

void Ant::step() {
  if (state_ == State::LOOKING_FOR_FOOD){
    moveRandom();
    if (grabFood()){
      foodAt_.push_back(location_);
      printf("Ant %d found food at %s!\n", id_, location_.toString().c_str());
      state_ = State::RETURNING_HOME;
    }
    askForFood();
  }
  printPosition();
}

bool Ant::grabFood() {
  if (world_.takeFoodFrom(location_))
    return true;
  else
    return false;
}

void Ant::askForFood() {
  auto neighborAnts = world_.ant_colony_.getAntsAt(location_);
  // TODO ask them for food
}

void Ant::moveRandom() {
  int r = rand() % 4;
  switch(r) {
    case 0:
      // right
      if (location_.x < world_.getXDimension()-1) location_.x += 1;
      break;
    case 1:
      // up
      if (location_.y < world_.getYDimension()-1) location_.y += 1;
      break;
    case 2:
      // left
      if (location_.x > 0) location_.x -= 1;
      break;
    case 3:
      // down
      if (location_.y > 0) location_.y -= 1;
      break;
    default:
      printf("Unexpected random number for moving of Ant! %d\n", r);
  }
}

bool Ant::isLookingForFood() const {
  return state_ == State::LOOKING_FOR_FOOD;
}

void Ant::printPosition() const {
  printf("Ant %d is at position %s\n", id_, location_.toString().c_str());
}

}  // namespace ant_colony
