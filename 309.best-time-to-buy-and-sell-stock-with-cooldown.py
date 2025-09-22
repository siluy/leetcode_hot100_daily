#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        hold = -prices[0]
        sold, rest = 0
        for p in prices[1:]:
            new_hold = max(hold, rest - p)
            new_sold = hold + p
            new_rest = max(rest, sold)
            hold, sold, rest = new_hold, new_sold, new_rest
        return max(sold, rest)
# @lc code=end

