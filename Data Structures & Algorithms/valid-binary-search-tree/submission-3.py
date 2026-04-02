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
      # Node, isLeft, floor, ceil
      q.append([root, True, float('-inf'), float('inf')])
      while q:
         node, isLeft, floor, ceil = q.popleft()
         if isLeft and (node.val <= floor or ceil <= node.val):
               return False
         elif not isLeft and (node.val <= floor or ceil <= node.val):
               return False
         if node.left:
            q.append([node.left, True, min(floor, node.val), node.val])
         if node.right:
            q.append([node.right, False, node.val, max(ceil, node.val)])
      return True
        