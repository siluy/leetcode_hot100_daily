#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0]*(n+1)
        max_side = 0
        for i in range(1, m+1):
            prev_diag = 0
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = 1 + min(dp[j-1], dp[j], prev_diag)
                    max_side = max(max_side, dp[j])
                else:
                    dp[j]=0
                prev_diag = temp
        return max_side*max_side
# @lc code=end

