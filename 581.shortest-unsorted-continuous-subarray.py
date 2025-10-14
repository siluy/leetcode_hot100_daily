#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, 0
        max_seen = float('-inf')
        min_seen = float('inf')
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]
        return max(0, right - left + 1)
# @lc code=end

