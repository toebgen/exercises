import unittest

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def problem01(numbers, k):
    summands_to_look_for = set()
    for number in numbers:
        if number in summands_to_look_for:
            return True
        else:
            summands_to_look_for.add(k-number)
    return False


class TestProblem01(unittest.TestCase):
    def test(self):
        test_cases = [
            ([10, 15, 3, 7],    17, True),
            ([10, 15, 3, 7],    10, True),
            ([10, 15, 3, 7],    13, True),
            ([10, 15, 3, 7],    22, True),
            ([10, 15, 3, 7],    25, True),
            ([9, 6],            15, True),
            ([0, 0, 0, 10, 5],  15, True),
            ([-3, 6],           3,  True),
            ([6, -3],           3,  True),
            ([0, 0, 0, 10],     10, True),
            ([10, 15, 3, 7],    5,  False),
            ([10, 15, 3, 7],    3,  False),
            ([5],               5,  False),
            ([],                5,  False),
        ]
        
        for numbers, k, result in test_cases:
            case_str = 'numbers={0}, k={1}, expected={2}'.format(numbers, k, result)
            print('Testing case:', case_str)
            self.assertEqual(problem01(numbers, k), result, msg=case_str)


if __name__ == '__main__':
    unittest.main()
