#pragma once

#include <vector>

#include "colony.h"
#include "location.h"

using namespace std;

namespace ant_colony {

class Colony;

/**
 * Represents the amount of food available on each grid cell.
 * E.g.:
 *    y
 *    ^
 *    | 0 2 0 0 0 0
 *    | 0 0 3 0 1 0
 *    | 0 0 0 0 0 0
 *    +-------------> x
 *  (0,0)
 */
class World {
  public:
    World(int x_dimension, int y_dimension, Colony& ant_colony);
  
    void placeFood(const Location loc, const int amount);    
    bool hasFood() const ;
    bool takeFoodFrom(const Location loc);
    int getAmountOfFoodAt(int x, int y) const;

    int getYDimension() const;
    int getXDimension() const;
    Location getHomeBase() const;

    Colony& ant_colony_;
  
  private:
    int x_dimension_, y_dimension_;
    vector<vector<int> > grid_;

    /// Total food amount available in whole grid
    int total_amount_food_available_;

    /// Location of ants' home base, i.e. where they are spawned and where
    /// they deliver the food
    Location ant_home_base_;
};

}  // namespace ant_colony
