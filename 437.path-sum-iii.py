#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix = {0: 1}
        # ans = 0
        # def dfs(node, cur):
        #     nonlocal ans
        #     if not node:
        #         return
        #     cur += node.val
        #     ans += prefix.get(cur - targetSum, 0)
        #     prefix[cur] = prefix.get(cur, 0) + 1
        #     dfs(node.left, cur)
        #     dfs(node.right, cur)
        #     prefix[cur] -= 1

        # dfs(root, 0)
        # return ans
        prefix = {0: 1}
        ans = 0
        def dfs(node, cur):
            nonlocal ans
            if not node:
                return 
            cur += node.val
            ans += prefix.get(cur - targetSum, 0)
            prefix[cur] = prefix.get(cur, 0) + 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1
        dfs(root, 0)
        return ans
# @lc code=end

