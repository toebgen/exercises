#pragma once

#include <memory>
#include <vector>

#include "ant.h"
#include "location.h"

using namespace std;

namespace ant_colony {

class Ant;

class Colony {
public:
  size_t getNumberOfAnts() const;
  vector<shared_ptr<Ant>> getAnts() const;
  vector<shared_ptr<Ant>> getAntsAt(const Location location) const;

  void addAnt(shared_ptr<Ant> ant);

private:
  vector<shared_ptr<Ant>> ants_;
};

} // namespace ant_colony