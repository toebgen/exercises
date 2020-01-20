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
  World(int x_dimension, int y_dimension, Colony &ant_colony);

  void placeFood(const Location &loc, const int amount);
  bool hasFood() const;
  bool isAllFoodCollected() const;
  bool takeFoodFrom(const Location &loc);
  void deliverFoodAtHomeBase();
  int getAmountOfFoodAt(const Location &loc) const;
  int getAmountOfFoodAt(int x, int y) const;

  Location getHomeBase() const;

  int getYDimension() const;
  int getXDimension() const;

  Colony &ant_colony_;

private:
  int x_dimension_, y_dimension_;

  /** Grid which holds the amonts of foods per grid cell */
  vector<vector<int>> grid_;

  /** Total food amount that is left in whole grid */
  int amount_food_left_;

  /** Amount of food that has already been delivered to home base */
  int amount_food_in_home_base_;

  /** Total amount of food that is in system (still available + in home
   * base) */
  int total_amount_food_in_system_;

  /** Location of ants' home base, i.e. where they are spawned and where
   * they deliver the food */
  Location ant_home_base_;
};

} // namespace ant_colony
