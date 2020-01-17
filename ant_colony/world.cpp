#include "world.h"

namespace ant_colony {

World::World(int x_dimension, int y_dimension, Colony& ant_colony) :
      x_dimension_(x_dimension),
      y_dimension_(y_dimension),
      amount_food_left_(0),
      amount_food_in_home_base_(0),
      ant_home_base_(Location(0, 0)),
      ant_colony_(ant_colony)
{
    grid_ = vector<vector<int> > (y_dimension, vector<int> (x_dimension, 0));
}

int World::getAmountOfFoodAt(const Location& loc) const {
    return getAmountOfFoodAt(loc.x, loc.y);
}

int World::getAmountOfFoodAt(int x, int y) const {
    return grid_.at(y).at(x);
}

int World::getXDimension() const { return x_dimension_; }

int World::getYDimension() const { return y_dimension_; }

Location World::getHomeBase() const { return ant_home_base_; }

void World::placeFood(const Location& loc, const int amount) {
    grid_.at(loc.y).at(loc.x) = amount;
    amount_food_left_ += amount;
    total_amount_food_in_system_ += amount;

    printf("Placed %d food at %s. Total in the world is %d.\n",
        amount, loc.toString().c_str(), total_amount_food_in_system_);
}

bool World::hasFood() const {
    if (amount_food_left_ > 0)
        return true;
    else
        return false;
}

bool World::isAllFoodCollected() const {
    return (total_amount_food_in_system_ == amount_food_in_home_base_);
}

bool World::takeFoodFrom(const Location& loc) {
    if (getAmountOfFoodAt(loc.x, loc.y) > 0) {
        grid_.at(loc.y).at(loc.x) -= 1;
        amount_food_left_ -= 1;

        printf("1 food has been taken from location %s. %d left here, %d left in total!\n",
            loc.toString().c_str(),
            getAmountOfFoodAt(loc), amount_food_left_);

        return true;
    }
    
    return false;
}

void World::deliverFoodAtHomeBase() {
    amount_food_in_home_base_++;
}

}  // namespace ant_colony
