/**
 * "Ant Colony"
 * 
 * The goal is to implement a colony of ants gathering food for their tribe.
 *
 * Rules:
 * - If you don't know where food is, try to find some.
 * - If you see another ants, ask if they know where food is.
 * - If you find food, take it back to the home.
 * - If you don't find any food where you thought, start searching again.
 */

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

struct Location {
  Location() : x(-1), y(-1) {}
  Location(const int x, const int y) : x(x), y(y) {}

  string toString() const {
    std::stringstream ss;
    ss << '[' << x << ", " << y << ']';
    return ss.str();
  }

  int x, y;
};

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
    World(int x_dimension, int y_dimension) :
      total_amount_food_available_(0),
      ant_home_base_(0, 0)
    {
      grid_ = vector<vector<int> > (y_dimension, vector<int> (x_dimension, 0));
    }
  
    void placeFood(const Location loc, const int amount) {
      grid_.at(loc.y).at(loc.x) = amount;
      total_amount_food_available_ += amount;
    }
    
    bool hasFood() const {
      if (total_amount_food_available_ > 0)
        return true;
      else
        return false;
    }

    bool takeFoodFrom(const Location loc) {
      if (getAmountOfFoodAt(loc.x, loc.y) > 0) {
        grid_.at(loc.y).at(loc.x) -= 1;
        total_amount_food_available_ -= 1;
        return true;
      }
      
      return false;
    }
  
    int getAmountOfFoodAt(int x, int y) const { return grid_.at(y).at(x); }
    int getYDimension() const { return size(grid_); }
    int getXDimension() const { return size(grid_.at(0)); }
    Location getHomeBase() const { return ant_home_base_; }
  
  private:
    vector<vector<int> > grid_;
    int total_amount_food_available_;  //!< Total food amount available in whole grid
    Location ant_home_base_;
};

class Ant {
  public:
    Ant(World& world, int id = -1) :
      world_(world),
      id_(id),
      state_(Ant::State::LOOKING_FOR_FOOD)
      {
        location_ = world_.getHomeBase();
      }
    
    enum class State {LOOKING_FOR_FOOD, RETURNING_HOME};
    
    void step(){
      if (state_ == State::LOOKING_FOR_FOOD){
        moveRandom();
        if (isFoodAvailableHere()){
          printf("Ant %d found food at %s!\n", id_, location_.toString().c_str());
          state_ = State::RETURNING_HOME;
        }
      }
      printPosition();
      
    }
    
    bool isFoodAvailableHere() {
      if (world_.takeFoodFrom(location_)) {
        foodAt_.push_back(location_);
        return true;
      } else {
        return false;
      }
    }
    
    void moveRandom(){
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

    void printPosition() const {
      printf("Ant %d is at position %s\n", id_, location_.toString().c_str());
    }

    bool isLookingForFood() const { return state_ == State::LOOKING_FOR_FOOD; }
  
  private:
    int id_;  //!< Ant ID
    Location location_;  //!< Ant Location in World coordinates
    State state_;

    vector<Location> foodAt_;  //!< Locations known to have food

    World& world_;
};

class Simulator {
  public :
  Simulator (World& world) :
    world_(world),
    ant_counter_(0)
    {};

  void createAnt() {
    shared_ptr<Ant> new_ant = make_shared<Ant>(world_, ant_counter_++);
    ants_.push_back(new_ant);
  }

  void createAnts(const int numberOfAnts) {
    for (int i = 0; i < numberOfAnts; ++i)
      createAnt();
  }
  
  void step(){
    for (const auto ant : ants_) ant->step();
  };
  
  private:
    World& world_;

    vector<shared_ptr<Ant> > ants_;
    int ant_counter_;
};


int main() {
  printf("Starting program!\n");

  int x_dimension = 100, y_dimension = 100;
  World world(x_dimension, y_dimension);
  world.placeFood({50, 50}, 1);
  
  Simulator simulator(world);
  simulator.createAnts(1);
  
  int steps = 0, max_steps = 1000000;
  while (world.hasFood() && steps < max_steps) {
    simulator.step();
    steps++;
  }
  
  printf("=> steps: %d\n", steps);
  printf("Done\n");
  
  return 0;
}
