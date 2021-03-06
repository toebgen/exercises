#pragma once

#include <memory>
#include <set>

#include "location.h"
#include "world.h"

namespace ant_colony {

class World;

class Ant {
public:
  Ant(World &world, int id = -1);

  enum class State { LOOKING_FOR_FOOD, RETURNING_HOME, STATE_SIZE };

  enum class MovingDirection {
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3,
    MOVING_DIRECTION_SIZE = 4
  };

  Location getLocation() const;

  /**
   * Perform one cycle in the life of an Ant :-)
   * Find food, or bring food to the home base, respectively.
   * Always ask other ants for food locations on the way.
   */
  void step();

  /** Move in given direction */
  virtual void move(const MovingDirection moving_direction);
  /** Move in random direction */
  void moveRandom();
  /** Move towards given destination */
  void moveTowards(const Location &destination);

  /** Returns true if grabbing food from current location was successful */
  bool tryToGrabFood();
  /** Updates foodList_ with food locations from neighboring ants, if there
   * are any at the same location currently */
  void askForFood();
  /** Returns true, if size of foodList_ is > 0 */
  bool knowsFoodLocations() const;
  /** Returns true, if location_ is at home base */
  bool deliverFood();
  /** Returns set of all known food locations */
  std::set<Location> getFoodList() const;
  Location getNextFoodLocation() const;

  State getState() const;
  int getId() const;
  virtual string_view getType() const;

  string getFoodListAsStr() const;

protected:
  int id_;            //!< Ant ID
  Location location_; //!< Ant Location in World coordinates
  State state_;

  std::set<Location> foodList_; //!< Locations known to have food

  World &world_;

private:
};

/**
 * Quick Ant, that has a bigger step size than a regular Ant.
 * Design doesn't really make sense, that's just for practice...
 */
class QuickAnt : public Ant {
public:
  QuickAnt(World &world, int id = -1);

  virtual void move(const MovingDirection moving_direction);

  virtual string_view getType() const;

private:
  int step_size_;
};

} // namespace ant_colony
