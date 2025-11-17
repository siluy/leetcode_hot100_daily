#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1 = hold2 = float('-inf')
        sold1 = sold2 = 0
        for p in prices:
            hold1 = max(hold1, -p)
            sold1 = max(sold1, hold1 + p)
            hold2 = max(hold2, sold1 - p)
            sold2 = max(sold2, hold2 + p)
        return sold2
# @lc code=end

