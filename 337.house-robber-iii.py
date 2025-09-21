#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_skip, left_rob) + max(right_rob, right_skip)
            return (rob_this, skip_this)
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
# @lc code=end

