# LeetCode 172 trailingZeroes
# 题目：给定整数n，返回n!结果中末尾零的个数
# 核心思路：末尾零来自因子10，即因子2×5；2的数量总比5多，所以只需统计n!中含因子5的个数
# 踩坑：一开始想直接算阶乘再数0，但n一大就溢出；正确做法是不断累加 n//5、n//25、n//125...
# 时间复杂度：O(log n)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n > 0:
            n = n // 5
            ans += n
        return ans
