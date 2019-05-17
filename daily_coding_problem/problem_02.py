import unittest

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def problem02(input):
    output, total_product = [], 1
    for element in input:
        total_product *= element
    output = [total_product/element for element in input]
    return output


class TestProblem02(unittest.TestCase):
    def test(self):
        test_cases = [
            ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
            ([3, 2, 1], [2, 3, 6]),
        ]
        
        for input, output in test_cases:
            case_str = 'input={0}, output={1}'.format(input, output)
            print('Testing case:', case_str)
            self.assertEqual(problem02(input), output, msg=case_str)


if __name__ == '__main__':
    unittest.main()
