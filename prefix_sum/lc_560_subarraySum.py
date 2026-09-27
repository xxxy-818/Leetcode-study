# LeetCode 560 subarraySum
# 题目：统计和为k的连续子数组个数
# 核心思路：前缀和 + 哈希表。子数组和 nums[i..j] = pre[j+1] - pre[i]，统计前缀和中"pre[i] = 当前前缀和 - k"出现次数
#   遍历前缀和，对每个num，看 num-k 出现过几次就加几次，再把当前前缀和计数+1
# 踩坑：不能只算前缀和再双重循环（O(n²)超时）；要用哈希表边遍历边记录前缀和出现次数，只需O(n)
# 时间复杂度：O(n)
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n+1)
        ans = 0
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
        cnt = defaultdict(int)
        for num in pre:
            need = num - k
            ans += cnt[need]
            cnt[num] += 1
        return ans
