#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, step in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + step)
        return True
# @lc code=end

