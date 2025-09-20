#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # total = sum(nums)
        # if total & 1:
        #     return False
        # target = total // 2
        # dp = [False] * (target + 1)
        # dp[0] = True
        # for x in nums:
        #     if x > target:
        #         continue
        #     for s in range(target, x - 1, -1):
        #         if dp[s - x]:
        #             dp[s] = True
        #         if dp[target]:
        #             return True
        # return dp[target]
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            if x > target:
                continue
            for s in range(target, x - 1, -1):
                if dp[s - x]:
                    dp[s] = True
                if dp[target]:
                    return True
        return dp[target]
# @lc code=end

