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
            # Current node is the smallest
            if not curr.left:
                k-=1
                if k == 0:
                    return curr.val
                curr = curr.right
            # You have smaller nodes
            else:
                prev = curr.left
                while prev.right and prev.right!=curr:
                    prev = prev.right
                # First time visiting the rightmost node
                # Connect it with the current node in a layer above
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                # Second time visiting the rightmost node while coming up
                else:
                    prev.right = None
                    k -=1
                    if k == 0:
                        return curr.val
                    # The current is at the sub-root node, and we must have worked on the left subtree, therefore the next smallest is on your right
                    curr = curr.right
                