#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                if dp[i] > dp[i - sq] + 1:
                    dp[i] = dp[i - sq] + 1
        return dp[n]
# @lc code=end

