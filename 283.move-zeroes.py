#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read, v in enumerate(nums):
            if v != 0:
                if write != read:
                    nums[write] = v
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
# @lc code=end

