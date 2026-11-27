# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter depth of left and right
        # Also need so far max
        self.res = 0
        def dfs(node):
            if not node:
                return 0

            l, r = dfs(node.left), dfs(node.right)
            diameter = l + r
            self.res = max(self.res, diameter)

            depth = 1 + max(l, r)
            return depth

        dfs(root)
        return self.res 