# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            l, lmax = dfs(root.left)
            r, rmax = dfs(root.right)
            return 1+ max(l, r), max(l+r, max(lmax, rmax))
        a, res = dfs(root)
        return res
    