# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            
            l, LisBalanced = dfs(node.left) 
            r, RisBalanced = dfs(node.right)
            
            if not LisBalanced or not RisBalanced or abs(l - r) > 1:
                return -1, False
            else:
                return 1 + max(l, r), True

        _, res = dfs(root)
        return res
