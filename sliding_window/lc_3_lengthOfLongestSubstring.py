# LeetCode 3 lengthOfLongestSubstring
# 题目：求字符串s中，不含重复字符的最长子串长度
# 核心思路：滑动窗口 + 哈希计数。right指针扩展窗口，遇到重复字符时用while收缩left，直到当前字符不重复，再更新最大长度
# 踩坑：一开始想用set判断，但没法记录每个字符出现次数，重复时不知道要移动left到哪；改用defaultdict计数，重复时就逐步收缩
# 时间复杂度：O(n)（左右指针各走一遍）
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqmap = defaultdict(int)
        left = 0
        n = len(s)
        max_len = 0
        for right in range(n):
            ch = s[right]
            freqmap[ch] += 1
            while freqmap[ch] > 1:
                left_ch = s[left]
                freqmap[left_ch] -= 1
                left += 1
            win_len = right - left + 1
            if win_len > max_len:
                max_len = win_len
        return max_len
