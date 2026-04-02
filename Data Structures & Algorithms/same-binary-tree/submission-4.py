# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            f, s = q1.popleft(), q2.popleft()
            if f and s and f.val == s.val:
                q1.append(f.left)
                q1.append(f.right)
                q2.append(s.left)
                q2.append(s.right)
            elif not f and not s:
                continue
            else:
                return False     
        return True