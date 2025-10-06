#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
# @lc code=end

