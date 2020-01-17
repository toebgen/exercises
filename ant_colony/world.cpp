#include "world.h"

namespace ant_colony {

World::World(int x_dimension, int y_dimension, Colony& ant_colony) :
      x_dimension_(x_dimension),
      y_dimension_(y_dimension),
      total_amount_food_available_(0),
      ant_home_base_(Location(0, 0)),
      ant_colony_(ant_colony)
{
    grid_ = vector<vector<int> > (y_dimension, vector<int> (x_dimension, 0));
}

int World::getAmountOfFoodAt(int x, int y) const {
    return grid_.at(y).at(x);
}

int World::getYDimension() const { return x_dimension_; }

int World::getXDimension() const { return y_dimension_; }

Location World::getHomeBase() const { return ant_home_base_; }

void World::placeFood(const Location loc, const int amount) {
    grid_.at(loc.y).at(loc.x) = amount;
    total_amount_food_available_ += amount;
}

bool World::hasFood() const {
    if (total_amount_food_available_ > 0)
        return true;
    else
        return false;
}

bool World::takeFoodFrom(const Location loc) {
    if (getAmountOfFoodAt(loc.x, loc.y) > 0) {
        grid_.at(loc.y).at(loc.x) -= 1;
        total_amount_food_available_ -= 1;
        return true;
    }
    
    return false;
}

}  // namespace ant_colony
