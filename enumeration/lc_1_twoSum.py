# LeetCode 1 twoSum
# 题目：找出数组中两数之和等于target的下标
# 核心思路：哈希表。遍历时记录每个数及其下标，对当前num查 target-num 是否已出现过
# 踩坑：暴力双重循环O(n²)超时；用哈希表边存边查只需O(n)，注意先查再存，避免同一元素重复用
# 时间复杂度：O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in needs:
                return [needs[need], i]
            needs[num] = i
