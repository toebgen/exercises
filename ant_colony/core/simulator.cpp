#include "simulator.h"

#include <memory>

#include <plog/Log.h>

#include "ant.h"
#include "world.h"

namespace ant_colony {

Simulator::Simulator(World &world) : world_(world){};

void Simulator::createAnt() {
  shared_ptr<Ant> new_ant =
      make_shared<Ant>(world_, world_.ant_colony_.getNumberOfAnts() + 1);

  PLOG_VERBOSE << "Created ant of type " << typeid(new_ant).name();
  world_.ant_colony_.addAnt(new_ant);
}

void Simulator::createAnts(const int numberOfAnts) {
  for (int i = 0; i < numberOfAnts; ++i)
    createAnt();
}

void Simulator::createQuickAnt() {
  shared_ptr<Ant> new_ant =
      make_shared<QuickAnt>(world_, world_.ant_colony_.getNumberOfAnts() + 1);

  world_.ant_colony_.addAnt(new_ant);
}

void Simulator::step() {
  for (const auto ant : world_.ant_colony_.getAnts()) {
    // PLOG_VERBOSE << "Calling step on Ant " << ant->getId() << ", type "
    //              << typeid(ant).name() << ", getType(): " << ant->getType();
    ant->step();
  }
} // namespace ant_colony

} // namespace ant_colony
