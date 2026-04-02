# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
         if not root:
            return 0

         res = 0
         q = deque([(root, float('-inf'))])
         while q:
            node, sofar = q.popleft()
            res += 1 if node.val >= sofar else 0
            sofar = max(sofar, node.val)
            if node.left:
               q.append((node.left, sofar))
            if node.right:
               q.append((node.right, sofar))
         return res