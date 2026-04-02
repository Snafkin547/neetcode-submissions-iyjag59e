# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      if not root:
         return True
      q = deque()
      # Node, floor, ceil
      q.append([root, float('-inf'), float('inf')])
      while q:
         node, floor, ceil = q.popleft()
         if not floor < node.val < ceil:
               return False
         if node.left:
            q.append([node.left, floor, node.val])
         if node.right:
            q.append([node.right, node.val, ceil])
      return True
        