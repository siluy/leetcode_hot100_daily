#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def dfs(index, remain):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                val = candidates[i]
                if val > remain:
                    break
                path.append(val)
                dfs(i, remain - val)
                path.pop()
        dfs(0, target)
        return res
# @lc code=end

