#pragma once

namespace ant_colony {

class World;

class Simulator {
public:
  Simulator(World &world);

  void createAnt();
  void createAnts(const int numberOfAnts);

  void createQuickAnt();

  void step();

private:
  World &world_;
};

} // namespace ant_colony
