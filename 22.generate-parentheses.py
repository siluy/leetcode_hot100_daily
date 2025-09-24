#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(open_used, close_used):
            if open_used == n and close_used == n:
                res.append("".join(path))
                return
            if open_used < n:
                path.append('(')
                dfs(open_used + 1, close_used)
                path.pop()
            if close_used < open_used:
                path.append(')')
                dfs(open_used, close_used + 1)
                path.pop()
        dfs(0, 0)
        return res
# @lc code=end

