# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_max, l_longer = dfs(node.left)
            r_max, r_longer = dfs(node.right)
            return max(l_longer + r_longer, max(l_max, r_max)), 1 + max(l_longer, r_longer)
        sofar_max, un = dfs(root)
        return sofar_max