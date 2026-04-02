# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # From bottom to upward, at each node, check if p existed in left and q in right
        def dfs(node, small, large):
            if not node:
                return False
            
            left = dfs(node.left, small, large)
            right = dfs(node.right, small, large)
            nonlocal res

            if left and right:
                res = node
                return False
            
            elif left or right:
                if node.val == large.val or node.val == small.val:
                    res = node
                    return False
                return True

            elif node.val == small.val or node.val == large.val:
                return True
 
            return False

        res = None
        s = p if p.val < q.val else q
        l = p if p.val >= q.val else q
        dfs(root, s, l)
        return res
