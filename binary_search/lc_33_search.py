# LeetCode 33 search
# 题目：在旋转过的有序数组中查找target，找到返回下标，否则-1（数组元素互不相同）
# 核心思路：二分查找 + 判断有序区间。每次比较 nums[left] 与 nums[mid]，
#   若左半有序则判断target是否在左半，在就缩right，否则去右半；右半同理
# 关键：每次mid把数组分成两段，必有一段有序，用有序段判断target归属
# 踩坑：一开始直接普通二分，忽略了数组被旋转，nums[mid]和target比较不单调，判断条件容易写反；
#   要额外判断 nums[left]<=nums[mid] 判断哪段有序，且边界用 <= 和 < 要小心
# 时间复杂度：O(log n)
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
