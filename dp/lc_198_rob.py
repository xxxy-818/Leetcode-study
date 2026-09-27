# LeetCode 198 rob
# 题目：一排房子各有金额，不能偷相邻两间，求能偷到的最大金额
# 核心思路：动态规划。dp[i]表示偷前i间房的最大金额，dp[i] = max(不偷第i间 dp[i-1], 偷第i间 nums[i-1]+dp[i-2])
#   状态：dp[0]=0不偷任何，dp[1]=nums[0]只偷第一间
# 踩坑：容易搞混下标，nums是0-indexed而dp是1-indexed，取nums[i-1]时容易错；先理清dp[i]对应前i间房
# 时间复杂度：O(n)
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[n]
