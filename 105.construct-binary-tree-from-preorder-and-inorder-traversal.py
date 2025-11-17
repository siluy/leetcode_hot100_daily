#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)
        def helper(left, right):
            if left > right:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            mid = idx[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(inorder) - 1)

# @lc code=end

