#include "simulator.h"

#include <memory>

#include "ant.h"
#include "world.h"

namespace ant_colony {

Simulator::Simulator (World& world) :
    world_(world)
    {};

void Simulator::createAnt() {
    shared_ptr<Ant> new_ant = make_shared<Ant>(world_,
        world_.ant_colony_.getNumberOfAnts() + 1);

    world_.ant_colony_.addAnt(new_ant);
}

void Simulator::createAnts(const int numberOfAnts) {
    for (int i = 0; i < numberOfAnts; ++i)
        createAnt();
}

void Simulator::step(){
    for (const auto ant : world_.ant_colony_.getAnts())
        ant->step();
}


}  // namespace ant_colony
