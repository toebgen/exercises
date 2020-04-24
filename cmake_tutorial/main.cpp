#ifndef CMAKEMACROSAMPLE
#define CMAKEMACROSAMPLE "NO SYSTEM NAME"
#endif

#include "lib/math/operations.hpp"
#include <iostream>

int main() {
  std::cout << "Hello CMake!"
            << " We are on a " << CMAKEMACROSAMPLE << " system!" << std::endl;

  math::operations op;
  int sum = op.sum(3, 4);
  std::cout << "Sum of 3+4: " << sum << std::endl;
}
