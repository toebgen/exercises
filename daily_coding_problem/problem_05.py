import unittest

"""
Problem #5 [Medium]
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""


def cons(a, b):
    # Closure: Outer enclosing function
    def pair(f):
        # Nested function
        return f(a, b)
    return pair


def car(c):
    return c(lambda a, b: (a, b))[0]


def cdr(c):
    return c(lambda a, b: (a, b))[1]


class TestProblem05(unittest.TestCase):
    def test(self):
        # cons_1 = cons(3, 4)
        # print(cons_1(lambda a, b: (a, b))[0])
        # print(cons_1(lambda a, b: (a, b))[1])

        self.assertEqual(car(cons(3, 4)), 3)
        self.assertEqual(cdr(cons(3, 4)), 4)


if __name__ == '__main__':
    unittest.main()
