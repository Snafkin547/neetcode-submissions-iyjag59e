# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if val is same and true is returned from both
        first = [p]
        second = [q]
        while first and second:
            f = first.pop()
            s = second.pop()

            if (not f and not s):
                continue
            elif f and s and f.val == s.val:
                first.append(f.left)
                first.append(f.right)
                second.append(s.left)
                second.append(s.right)
            else:
                return False

        return not first and not second
