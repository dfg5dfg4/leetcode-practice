/**
 * LeetCode #1: Two Sum
 * 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
 */

#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    /**
     * 解法：使用哈希表存储已经遍历过的元素及其索引
     * 时间复杂度：O(n)
     * 空间复杂度：O(n)
     */
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            map[nums[i]] = i;
        }
        
        // 如果没有找到结果，返回空数组（实际上题目保证有解，所以不会执行到这里）
        return {};
    }
};

// 测试代码
int main() {
    Solution solution;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    
    std::vector<int> result = solution.twoSum(nums, target);
    std::cout << "[" << result[0] << ", " << result[1] << "]" << std::endl; // 应该输出 [0, 1]
    
    return 0;
}