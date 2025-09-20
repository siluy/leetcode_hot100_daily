#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # INF = amount + 1
        # dp = [INF] * (amount + 1)
        # dp[0] = 0
        # for a in range(1, amount + 1):
        #     for c in coins:
        #         if a >= c:
        #             dp[a] = min(dp[a], dp[a - c] + 1)
        # return -1 if dp[amount] == INF else dp[amount]
        INF = amount +1
        dp = [INF] * (amount+1)
        dp[0]=0
        for a in range(1, amount+1):
            for c in  coins:
                if a>=c:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return -1 if dp[amount] == INF else dp[amount]
# @lc code=end

