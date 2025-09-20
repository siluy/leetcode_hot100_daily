#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for v in nums:
            x ^= v 
        return x
# @lc code=end

