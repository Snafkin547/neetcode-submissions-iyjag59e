# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # From bottom to upward, at each node, check if p existed in left and q in right
        def dfs(node):
            if not node:
                return

            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            elif left or right:
                return left if left else right
            else:
                return

        return dfs(root)
