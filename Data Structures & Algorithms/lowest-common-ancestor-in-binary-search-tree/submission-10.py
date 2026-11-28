# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        def dfs(node):
            if not node:
                return False
            nonlocal res

            l = dfs(node.left)
            r = dfs(node.right)
            m = node == p or node == q
            if l + r + m >= 2:
                res = node
            return l or r or m
        dfs(root)
        return res
        