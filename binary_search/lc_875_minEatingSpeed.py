# LeetCode 875 minEatingSpeed
# 题目：求能在h小时内吃完所有香蕉的最小速度d（每小时吃d根，每堆不足d根也花1小时）
# 核心思路：二分答案。吃完整堆所需小时数 sum(pile/d向上取整)，对速度d单调递减，
#   二分找满足 check(d)<=h 的最小速度，满足就收窄right，不满足就加大left
# 踩坑：向上取整写成 (pile+d-1)//d 时容易溢出或边界错，用 整除+余数判断 更稳；
#   初始left从1开始（速度为0无意义），right设为sum(piles)足够
# 时间复杂度：O(n log S)，S为总香蕉数
from typing import List

def check(d, piles, h):
    h1 = 0
    for pile in piles:
        h1 += pile // d + 1 if pile % d != 0 else pile // d
    return h1 <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid, piles, h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
