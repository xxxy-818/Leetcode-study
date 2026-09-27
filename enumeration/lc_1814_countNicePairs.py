# LeetCode 1814 countNicePairs
# 题目：统计满足 nums[i]+rev(nums[j]) == nums[j]+rev(nums[i]) 的(i,j)对数
# 核心思路：变形 + 哈希计数。原式移项得 nums[i]-rev(nums[i]) == nums[j]-rev(nums[j])，
#   即差值相同即可配对。对每个num计算差值num-rev(num)，用哈希表计数，同差值v个可配 v*(v-1)/2 对
# 踩坑：反转数字可以转字符串[::-1]，但大数转str慢；自己写rev循环时容易在"一位数"边界出错；
#   别忘了答案要 mod 1e9+7
# 时间复杂度：O(n·k)，k为数字位数
from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            reserve = int(str(num)[::-1])
            mp[num - reserve] += 1
        res = 0
        for v in mp.values():
            if v > 1:
                res += v * (v-1) // 2
        return res % (10**9 + 7)
