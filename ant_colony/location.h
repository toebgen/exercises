// #pragma once

#ifndef LOCATION_H_
#define LOCATION_H_

#include <string>
#include <sstream>

using namespace std;

/** x and y coordinate */
struct Location {
  Location() : x(-1), y(-1) {}
  Location(const int x, const int y) : x(x), y(y) {}

  std::string toString() const {
    std::stringstream ss;
    ss << '[' << x << ", " << y << ']';
    return ss.str();
  }

  int x, y;
};

inline bool operator==(const Location& lhs, const Location& rhs) {
  return (lhs.x == rhs.x) && (lhs.y == rhs.y);
}

#endif
