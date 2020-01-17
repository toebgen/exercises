#pragma once

#include <memory>
#include <vector>

#include "location.h"
#include "world.h"

namespace ant_colony {

class World;

class Ant {
  public:
    Ant(World& world, int id = -1);
    
    enum class State {LOOKING_FOR_FOOD, RETURNING_HOME};

    Location getLocation() const;
    
    void step();    
    
    bool grabFood();
    void askForFood();
    
    void moveRandom();
    
    void printPosition() const;

    bool isLookingForFood() const;
  
  private:
    int id_;  //!< Ant ID
    Location location_;  //!< Ant Location in World coordinates
    State state_;

    std::vector<Location> foodAt_;  //!< Locations known to have food

    World& world_;
};

}  // namespace ant_colony
