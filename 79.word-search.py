#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[idx]:
                return False
            tmp, board[r][c] = board[r][c], '#'
            found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
            board[r][c] = tmp
            return found
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False

# @lc code=end

