#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(arr):
            prev = cur = 0
            for val in arr:
                prev, cur = cur, max(prev + val, cur)
            return cur
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))
# @lc code=end

