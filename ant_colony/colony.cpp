#include "colony.h"

namespace ant_colony {

size_t Colony::getNumberOfAnts() const {
    return ants_.size();
}

void Colony::addAnt(shared_ptr<Ant> ant) {
    ants_.push_back(ant);
}

vector<shared_ptr<Ant> > Colony::getAnts() const {
    return ants_;
}

vector<shared_ptr<Ant> > Colony::getAntsAt(Location location) const {
    vector<shared_ptr<Ant> > relevant_ants;
    for (const auto ant : ants_) {
        if (ant->getLocation() == location) relevant_ants.push_back(ant);
    }
    return relevant_ants;
}

}  // namespace ant_colony
