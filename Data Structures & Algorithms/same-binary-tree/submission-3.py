# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            f, s = stack.pop()
            if f and s and f.val == s.val:
                stack.append((f.left, s.left))
                stack.append((f.right, s.right))
            elif not f and not s:
                continue
            else:
                return False     
        return True