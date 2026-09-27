# LeetCode 209 minSubArrayLen
# 题目：找出数组中，和 ≥ target 的连续子数组的最小长度，没有则返回0
# 核心思路：滑动窗口。right向右扩展累加，一旦 total≥target 就收缩left找更短窗口，同时更新最小长度
# 踩坑：一开始漏了"没有满足条件的子数组返回0"的情况，直接返回了inf；要用inf做哨兵，判断后转成0
# 时间复杂度：O(n)
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float('inf')
        total = 0
        for right in range(n):
            total += nums[right]
            while total >= target:
                win_len = right - left + 1
                min_len = min(min_len, win_len)
                total -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
