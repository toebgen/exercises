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
#include <vector>

using namespace std;


class World {
  public:
    World(int x_dimension, int y_dimension){
      grid_ = vector<vector<int> > (y_dimension, vector<int> (x_dimension, 0));
    }
  
    void placeFood(int x, int y, int amount) {
      grid_.at(y).at(x) = amount;
    }
    
    bool hasFood() const {
      for (const auto& y : grid_) {
        for (const auto& x : y) {
          if (x > 0) return true;
        }
      }

      return false;
    }

    bool takeFoodFrom(int x, int y) {
      if (getAmountOfFoodAt(x, y) > 0) {
        grid_.at(y).at(x) -= 1;
        return true;
      }
      
      return false;
    }
  
    int getAmountOfFoodAt(int x, int y) const {
      return grid_.at(y).at(x);
    }

    int getYDimension() const {
      return size(grid_);
    }

    int getXDimension() const {
      return size(grid_.at(0));
    }
  
  private:
    /**
     * Grid represents the amount of food available on each grid cell.
     * E.g.:
     *    y
     *    ^
     *    | 0 2 0 0 0 0
     *    | 0 0 3 0 1 0
     *    | 0 0 0 0 0 0
     *    +-------------> x
     *  (0,0)
     */
    vector<vector<int> > grid_;
};

class Ant {
  public:
    Ant(World& world) :
      world_(world),
      x_(0), y_(0),
      looking_for_food(true) {}
    
    void step(){
      moveRandom();
      printPosition();
      if (checkForFood()){
        printf("Ant %d found food at [%d, %d]!\n", id_, x_, y_);
      }
    }
    
    bool checkForFood() {
      if (world_.takeFoodFrom(x_, y_)) {
        looking_for_food = false;
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
          if (x_ < world_.getXDimension()-1) x_ += 1;
          break;
        case 1:
          // up
          if (y_ < world_.getYDimension()-1) y_ += 1;
          break;
        case 2:
          // left
          if (x_ > 0) x_ -= 1;
          break;
        case 3:
          // down
          if (y_ > 0) y_ -= 1;
          break;
        default:
          printf("Unexpected random number for moving of Ant! %d\n", r);
      }
    }

    void printPosition() const {
      printf("Ant %d is at position [%d, %d]\n", id_, x_, y_);
    }

    bool lookingForFood() const { return looking_for_food; }
  
  private:
    World& world_;

    int id_;    
    int x_, y_;
    
    bool looking_for_food;
};

class Simulator {
  public :
  Simulator (World& world, Ant& ant) : world_(world), ant_(ant) {};
  
  void step(){
    ant_.step();
  };
  
  private:
    World& world_;
    Ant& ant_;
};


int main() {
  printf("Starting program!\n");

  // for (int i=0; i<25; ++i) {
  //   int r = rand() % 4 + 1;
  //   printf("random number=%d\n", r);
  // }

  int x_dimension = 100, y_dimension = 100;
  World world(x_dimension, y_dimension);
  world.placeFood(50, 50, 1);
  
  Ant ant(world);
  Simulator simulator(world, ant);
  
  int steps = 0, max_steps = 1000000;
  while (world.hasFood() && steps < max_steps) {
    simulator.step();
    steps++;
  }
  
  printf("=> steps: %d\n", steps);
  printf("Done\n");
  
  return 0;
}
