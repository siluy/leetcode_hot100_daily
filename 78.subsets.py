#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(idx):
            res.append(path[:])
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
# @lc code=end

