#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # s = set(nums)
        # longest = 0 
        # for x in s:
        #     if x - 1 not in s:
        #         y = x + 1
        #         while y in s:
        #             y += 1
        #         longest = max(longest, y - x)
        # return longest
        s = set(nums)
        longest = 0
        for x in s:
            if x - 1 not in s:
                y = x +1
                while y in s:
                    y += 1
                longest = max(longest, y-x)
        return longest
# @lc code=end

