# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Need to know depths of l and r
        # Return False if abs(l - r) > 1
        res = True
        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            if abs(l - r) > 1:
                res = False 
            return 1 + max(l, r)
        dfs(root)
        return res