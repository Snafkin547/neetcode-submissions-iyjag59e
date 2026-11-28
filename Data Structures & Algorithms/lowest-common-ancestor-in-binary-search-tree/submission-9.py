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
            if ((node == p or node == q) and (dfs(node.left) or dfs(node.right))) or (dfs(node.left) and dfs(node.right)) :
                res = node
            return dfs(node.left) or dfs(node.right) or node == p or node == q
        dfs(root)
        return res
        