#ifndef CMAKEMACROSAMPLE
#define CMAKEMACROSAMPLE "NO SYSTEM NAME"
#endif

#include <boost/random.hpp>
#include <iostream>

#include "lib/math/operations.hpp"

int main() {
  std::cout << "Hello CMake!"
            << " We are on a " << CMAKEMACROSAMPLE << " system!" << std::endl;

  math::operations op;
  int sum = op.sum(3, 4);
  std::cout << "Sum of 3+4: " << sum << std::endl;

  // Boost random example
  boost::mt19937 rng;
  double mean = 2.4;
  double std = 1.97;
  auto normal_distribution =
      boost::random::normal_distribution<double>(mean, std);

  boost::variate_generator<boost::mt19937 &, boost::normal_distribution<>>
      random_generator(rng, normal_distribution);

  for (int i = 0; i < 2; ++i) {
    auto rand_val = random_generator();
    std::cout << "Random value " << i + 1 << ": " << rand_val << std::endl;
  }

  return 0;
}
