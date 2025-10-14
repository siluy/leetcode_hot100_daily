#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = grid[i-1][j] if i > 0 else float('inf')
                left = grid[i][j-1] if j > 0 else float('inf')
                grid[i][j] += min(top, left)
        return grid[m-1][n-1]
# @lc code=end

