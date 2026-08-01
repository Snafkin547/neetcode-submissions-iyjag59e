# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = p.val if p.val < q.val else q.val
        large = p.val if p.val >= q.val else q.val
        def dfs(node):
            if not node:
                return None
            if small <= node.val <= large:
                return node
            elif large < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)



        