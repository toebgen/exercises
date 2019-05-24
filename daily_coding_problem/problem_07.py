import itertools
from collections import defaultdict
from string import ascii_lowercase
import unittest

"""
Problem #7 [Medium]
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]


def num_decodings(input):
    if len(input) <= 1:
        return 1
    elif input.startswith('0'):
        return 0

    total = 0

    if int(input[:2]) <= 26:
        total += num_decodings(input[2:])
    
    total += num_decodings(input[1:])

    return total


class TestProblem07(unittest.TestCase):
    def test(self):
        test_cases = [
            ('127', 2),  # abg, lg
            ('111', 3),  # aaa, ka, ak
            ('11', 2),   # aa, k
            ('1', 1),    # a
            ('26', 2),   # bf, z
            ('27', 1),   # bg
        ]

        for input, output in test_cases:
            case_str = 'input={0}, output={1}'.format(input, output)
            print('Testing case:', case_str)
            self.assertEqual(num_decodings(input), output, msg=case_str)
            

if __name__ == '__main__':
    unittest.main()
