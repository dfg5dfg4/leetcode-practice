# LeetCode #56: 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
 
import math
from typing import List

class Solution:
    """
    解法：排序若干个区间，然后按照顺序合并区间
    时间复杂度：O(nlogn)，主要是排序的时间复杂度
    空间复杂度：O(n)，需要存储结果数组
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先排序
        intervals.sort(key=lambda x: x[0])
        last = None
        result = []
        for cur in intervals:
            if last != None and cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                result.append(cur)
                last = cur
        return result


# 测试代码
if __name__ == "__main__":
    # 主函数入口
    solution = Solution()
    # 测试用例
    test_cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]]
    ]
    for intervals in test_cases:
        print(f"输入: {intervals}")
        print(f"输出: {solution.merge(intervals)}")
        print("---")