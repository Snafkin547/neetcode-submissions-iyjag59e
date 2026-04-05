# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1 # Decrement cuz this root node is the smallest at a time
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                
                # First time visiting this right most node in the subtreee
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                    # Let the next iteration work on the predecessor/same node as prev is referencing
                
                # Second time/After clearing everything on the left of "Current" Node/not prev node cuz prev = curr.left
                else:
                    prev.right = None # Dereference the predecessor
                    k -= 1
                    if k == 0:
                        return curr.val # Unintuitive, but when we reach this last right end node, we must have gone through this node in the first if block
                    curr = curr.right # We have already worked on 
        return -1
                

                    