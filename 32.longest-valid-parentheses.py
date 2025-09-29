#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        base = -1
        best = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        best = max(best, i - stack[-1])
                    else:
                        best = max(best, i - base)
                else:
                    base = i
        return best
# @lc code=end

