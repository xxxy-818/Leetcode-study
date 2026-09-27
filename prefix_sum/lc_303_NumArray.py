# LeetCode 303 NumArray
# 题目：多次查询数组 nums[left..right] 的区间和
# 核心思路：前缀和。预处理前缀数组 sums，sumRange用 sums[right+1] - sums[left] 快速返回，每次查询O(1)
# 踩坑：下标容易错——pre[i]存的是nums[0..i-1]的和，所以求[left,right]要用 sums[right+1] - sums[left]，right要+1
# 时间复杂度：预处理O(n)，每次查询O(1)
class NumArray:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.sums = [0] * (n+1)
        for i in range(n):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
