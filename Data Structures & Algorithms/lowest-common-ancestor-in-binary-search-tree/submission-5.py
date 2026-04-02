# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        sm, lg = min(p.val, q.val), max(p.val, q.val)
        while node:
            if sm <= node.val <= lg:
                return node
            elif node.val < sm:
                node = node.right
            else:
                node = node.left
        return None

        