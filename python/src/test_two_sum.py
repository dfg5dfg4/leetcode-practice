# 测试 two_sum.py 的解决方案

import unittest
from two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])
    
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(self.solution.twoSum(nums, target), [2, 4])
    
    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])
    
    def test_zero_target(self):
        nums = [0, 4, 3, 0]
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), [0, 3])


if __name__ == "__main__":
    unittest.main()