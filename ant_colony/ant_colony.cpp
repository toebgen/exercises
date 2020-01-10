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
#include<vector>

using namespace std;


class World {
  public:
    World(int rows, int cols){
      rows_ = rows;
      cols_ = cols;
      grid_ = vector<vector<int> > (rows_, vector<int> (cols_, 0));
    }
  
    void placeFood(int row, int col, int amount) {
      grid_.at(row).at(col) = amount;
    }
    
    bool hasFood() const {
      for (int row = 0; row<rows_; ++row) {
        for (int col = 0; col<cols_; ++col) {
          if (grid_.at(row).at(col) > 0) return true;
        }
      }
      
      return false;
    }
  
    int amountFood(int row, int col) const {
      return grid_.at(row).at(col);
    }
  
  private:
  
  /** Grid represents the amount of food available on each grid cell. */
  vector<vector<int> > grid_;
  
  int rows_;
  int cols_;

};

class Ant {
  public:
  Ant(World& world, int max_row, int max_col) :
    world_(world),
    row_(0), col_(0),
    max_row_(max_row), max_col_(max_col), find_food(true) {}
  
  void step(){
    moveRandom();
    foundFood();
  }
  
  bool foundFood() {
    if (world_.amountFood(row_, col_) > 0) {
      find_food = false;
      return true;
    } else {
      return false;
    }
  }
  
  void moveRandom(){
    int r = rand() % 4 + 1;
    switch(r) {
      case 0:
        // hoch
        if (row_ < max_row_) row_ += 1;
        break;
      case 1:
        // rechts
        if (col_ < max_col_) col_ += 1;
        break;
      case 2:
        // runter
        if (row_ > 0) row_ -= 1;
        break;
      case 3:
        // links
        if (col_ > 0) col_ -= 1;
        break;
      default:
        ;
    }
    
  }
  
  private:
  World& world_;
  
  int row_;
  int col_;
  int max_row_;
  int max_col_;
  
  bool find_food;
};

class Simulator {
  public :
  Simulator (World& world, Ant& ant) : world_(world), ant_(ant) {};
  
  void run(){
    ant_.step();
  };
  
  private:
    World& world_;
    Ant& ant_;
};



int main() {
  int rows = 1000;
  int cols = 1000;
  World world(rows, cols);
  world.placeFood(100, 100, 1);
  
  Ant ant(world, rows, cols);
  
  Simulator simulator(world, ant);
  
   int steps = 0;
   while (world.hasFood()) {
     simulator.run();
     steps++;
   }
  
  printf("=> steps: %d\n", steps);
  printf("Done\n");
  
  return 0;
}
