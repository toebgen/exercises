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
#include <memory>
#include <string>
#include <vector>

#include "ant.h"
#include "colony.h"
#include "location.h"
#include "world.h"

using namespace std;

namespace ant_colony {

class Simulator {
  public :
  Simulator (World& world) :
    world_(world)
    {};

  void createAnt() {
    shared_ptr<Ant> new_ant = make_shared<Ant>(world_,
      world_.ant_colony_.getNumberOfAnts() + 1);

    world_.ant_colony_.addAnt(new_ant);
  }

  void createAnts(const int numberOfAnts) {
    for (int i = 0; i < numberOfAnts; ++i)
      createAnt();
  }
  
  void step(){
    for (const auto ant : world_.ant_colony_.getAnts()) ant->step();
  }
  
  private:
    World& world_;
};

}  // namespace ant_colony

int main() {
  printf("Starting program!\n");

  ant_colony::Colony ant_colony;

  int x_dimension = 100, y_dimension = 100;
  ant_colony::World world(x_dimension, y_dimension, ant_colony);
  world.placeFood({50, 50}, 1);
  
  ant_colony::Simulator simulator(world);
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
