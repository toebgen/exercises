// #pragma once

#ifndef LOCATION_H_
#define LOCATION_H_

#include <sstream>
#include <string>

using namespace std;

/** x and y coordinate */
struct Location {
  Location() : x(-1), y(-1) {}
  Location(const int x, const int y) : x(x), y(y) {}

  string toString() const {
    stringstream ss;
    ss << '[' << x << ", " << y << ']';
    return ss.str().c_str();
  }

  int x, y;
};

inline bool operator==(const Location &lhs, const Location &rhs) {
  return (lhs.x == rhs.x) && (lhs.y == rhs.y);
}

inline bool operator<(const Location &lhs, const Location &rhs) {
  return (lhs.x < rhs.x) || (lhs.y < rhs.y);
}

#endif
