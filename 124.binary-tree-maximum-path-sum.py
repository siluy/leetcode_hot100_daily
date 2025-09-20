#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # best = float('-inf')
        # def dfs(node: Optional[TreeNode]) -> int:
        #     nonlocal best
        #     if not node:
        #         return 0 
        #     left = max(0, dfs(node.left))
        #     right = max(0, dfs(node.right))
        #     best = max(best, node.val + left + right)
        #     return node.val + max(left, right)
        # dfs(root)
        # return best
        best = float('-inf')
        def dfs(node):
            nonlocal best
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            best = max(best, node.val + right + left)
            return node.val + max(left, right)
        dfs(root)
        return best
# @lc code=end

