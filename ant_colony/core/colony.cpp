#include "colony.h"

#include <plog/Log.h>

namespace ant_colony {

size_t Colony::getNumberOfAnts() const { return ants_.size(); }

void Colony::addAnt(shared_ptr<Ant> ant) { ants_.push_back(ant); }

vector<shared_ptr<Ant>> Colony::getAnts() const {
  //   for (const auto ant : ants_) {
  //     PLOG_VERBOSE << "Checking Ant " << ant->getId() << ", type "
  //                  << typeid(ant).name() << ", getType(): " <<
  //                  ant->getType();
  //   }
  return ants_;
}

vector<shared_ptr<Ant>> Colony::getAntsAt(Location location) const {
  vector<shared_ptr<Ant>> relevant_ants;
  for (const auto ant : ants_) {
    if (ant->getLocation() == location)
      relevant_ants.push_back(ant);
  }
  return relevant_ants;
}

} // namespace ant_colony
