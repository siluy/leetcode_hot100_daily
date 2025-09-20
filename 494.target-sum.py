#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # S = sum(nums)
        # if abs(target) > S or (S + target) % 2 != 0:
        #     return 0
        # P = (S + target) // 2

        # dp = [0] * (P + 1)
        # dp[0] = 1
        # for num in nums:
        #     for s in range(P, num - 1, -1):
        #         dp[s] += dp[s - num]
        # return dp[P]
        S = sum(nums)
        if abs(target) > S or (S + target) % 2 != 0:
            return 0
        P = (S + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            for s in range(P, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[P]
# @lc code=end

