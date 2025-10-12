#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        def largest(hist):
            stack = []
            ans = 0
            for i, h in enumerate(hist + [0]):
                while stack and hist[stack[-1]] > h:
                    height = hist[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    ans = max(ans, height * width)
                stack.append(i)
            return ans
        for row in matrix:
            for c, val in enumerate(row):
                heights[c] = heights[c] + 1 if val == '1' else 0
            best = max(best, largest(heights))
        return best
            

# @lc code=end

