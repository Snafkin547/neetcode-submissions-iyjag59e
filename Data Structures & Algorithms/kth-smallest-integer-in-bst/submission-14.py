# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        curr = 0

        def helper(node):
            nonlocal res, curr

            if not node or res:
                return
            
            helper(node.left)

            if res:
                return

            curr += 1
            if curr == k:
                res = node.val
                return
            
            helper(node.right)
        helper(root)
        return res