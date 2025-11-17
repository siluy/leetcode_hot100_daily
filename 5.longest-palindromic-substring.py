#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = end = 0
        def expand(l, r):
            nonlocal start, end
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > end - start:
                start = l + 1
                end = r - 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start:end + 1]
# @lc code=end

