#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + [x for x in nums if x > 0] + [1]
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        for len_ in range(2, n):
            for i in range (0, n - len_):
                j = i + len_
                best = 0
                ai, aj = arr[i], arr[j]
                for k in range(i + 1, j):
                    coins = dp[i][k] + dp[k][j] + ai * arr[k] * aj
                    if coins > best:
                        best = coins
                dp[i][j] = best
        return dp[0][n - 1]

# @lc code=end

