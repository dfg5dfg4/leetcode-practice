# LeetCode #1: Two Sum
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

from typing import List


class Solution:
    """
    解法：使用哈希表存储已经遍历过的元素及其索引
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 创建一个哈希表
        hash_map = {}
        
        # 遍历数组
        for i, num in enumerate(nums):
            # 计算互补数
            complement = target - num
            
            # 如果互补数在哈希表中，返回结果
            if complement in hash_map:
                return [hash_map[complement], i]
            
            # 将当前数字及其索引添加到哈希表
            hash_map[num] = i
        
        # 如果没有找到结果，返回空列表（实际上题目保证有解，所以不会执行到这里）
        return []


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    
    result = solution.twoSum(nums, target)
    print(result)  # 应该输出 [0, 1]