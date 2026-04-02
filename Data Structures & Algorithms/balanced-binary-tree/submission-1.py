# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return true false and max height
        def dfs(node):
            if not node:
                return True, 0
            lres, l = dfs(node.left)
            rres, r = dfs(node.right)
            return (lres and rres and (abs(l-r) <= 1)), 1 + max(l, r)
        res , x = dfs(root)
        return res
