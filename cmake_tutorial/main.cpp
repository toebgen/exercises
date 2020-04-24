#include <iostream>

#ifndef CMAKEMACROSAMPLE
#define CMAKEMACROSAMPLE "NO SYSTEM NAME"
#endif

auto sum(int a, int b) { return a + b; }

int main() {
  std::cout << "Hello CMake!"
            << " We are on a " << CMAKEMACROSAMPLE << " system!" << std::endl;

  std::cout << "Sum of 3+4: " << sum(3, 4) << std::endl;
}
