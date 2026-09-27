# LeetCode 62 uniquePaths
# 题目：m×n网格从左上到右下，只能向下/向右，共有多少条不同路径
# 核心思路：动态规划。dp[i][j]表示到达(i,j)的路径数，dp[i][j] = dp[i-1][j] + dp[i][j-1]
#   边界：第一行和第一列都只有1条路径，初始化全为1
# 踩坑：一开始初始化没处理边界，导致第一行/第一列计算错误；要先把首行首列都设为1
# 时间复杂度：O(m×n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
