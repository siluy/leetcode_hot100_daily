#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, val in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(val)
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return res
# @lc code=end

