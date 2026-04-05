# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        res = []

        def helper(node):
            if not node:
                return
            # Prioritize anything on left
            helper(node.left)
            # Work on current
            heapq.heappush(res, node.val)
            # Pop largest if excessing k
            if len(res) > k:
                res.pop()
            helper(node.right)

        helper(root)
        return res[-1]