# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack, qstack = [p], [q]
        
        while pstack and qstack:
            cp, cq = pstack.pop(), qstack.pop()
            
            if not cp and not cq:
                continue

            if cp and cq and cp.val == cq.val:
                pstack.append(cp.left)
                pstack.append(cp.right)
                qstack.append(cq.left)
                qstack.append(cq.right)
            else:
                return False

        return not pstack and not qstack