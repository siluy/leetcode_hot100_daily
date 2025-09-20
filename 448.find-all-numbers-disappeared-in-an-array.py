#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # for x in nums:
        #     idx = abs(x) - 1
        #     if nums[idx] > 0:
        #         nums[idx] = -nums[idx]
        # return [i + 1 for i, v in enumerate(nums) if v > 0]
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 1:
                nums[idx] = -nums[idx]
        return [i + 1 for i, v in enumerate(nums) if v > 0]

# @lc code=end