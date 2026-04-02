# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root, -101))
        res = 0
        while q:
           curr, currMax = q.popleft()
           if curr.val >= currMax:
              res+= 1
              currMax = curr.val
           if curr.left:
              q.append((curr.left, currMax))
           if curr.right:
              q.append((curr.right, currMax))
        return res
