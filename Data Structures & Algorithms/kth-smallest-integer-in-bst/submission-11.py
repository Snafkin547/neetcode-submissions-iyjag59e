# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None

        def helper(node, target):
            if not node:
                return 0

            nonlocal res
            
            left = helper(node.left, target)
            if left == -1:
                return -1

            if left + 1 == target:
                res = node.val
                return -1

            curr = left + 1

            right = helper(node.right, target - curr)
            if right == -1:
                return -1

            curr += right
            return curr

        helper(root, k)
        return res