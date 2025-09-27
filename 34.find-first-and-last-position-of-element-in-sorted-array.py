#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound():
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        left = lower_bound()
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        def upper_bound():
            l, r = left, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l - 1
        right = upper_bound()
        return [left, right]
# @lc code=end

