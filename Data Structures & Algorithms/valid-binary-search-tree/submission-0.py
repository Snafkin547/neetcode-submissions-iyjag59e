# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
          if not node:
              return [None, None, True]
          # return min and max so far
        
          left= dfs(node.left)
          right = dfs(node.right)
          currMin = min(node.val, left[0]) if left[0] else node.val
          currMax = max(node.val, right[1]) if right[1] else node.val
          res = (left[1] < node.val if left[1] else True) and (right[0] > node.val if right[0] else True) and left[2] and right[2]
          return [currMin, currMax, res]
        return dfs(root)[2]