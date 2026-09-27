# LeetCode 400 findNthDigit
# 题目：数字序列"123456789101112..."中第n位是什么数字
# 核心思路：先定位n在第几位数(1位/2位/3位...)区间，再算出具体数字，最后取该数字的某一位
#   第x位数区间：从start开始，每个数占x位，共count个数；用 n -= x*count 逐区间跳过
#   定位后：num = start + (n-1)//x 得到具体数字，idx = (n-1)%x 得到第几位
# 踩坑：一开始想直接把所有数拼成字符串再取，n一大就内存溢出；正确做法是用数学区间定位，O(log n)
# 时间复杂度：O(log n)
class Solution:
    def findNthDigit(self, n: int) -> int:
        x = 1          # 当前位数
        count = 9      # 当前位数区间共有多少个数
        start = 1      # 当前位数区间的起始数字
        while n > x * count:
            n -= x * count
            x += 1
            count *= 10
            start *= 10
        num = start + (n - 1) // x
        idx = (n - 1) % x
        return int(str(num)[idx])
