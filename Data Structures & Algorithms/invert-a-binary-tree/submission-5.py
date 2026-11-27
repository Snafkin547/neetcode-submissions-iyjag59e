# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # DFS: Swap
        # push left and right if not none
        q = [root]
        while q:
            node = q.pop()
            l = node.left
            r = node.right
            node.left, node.right = r, l
            if l:
                q.append(l)
            if r:
                q.append(r)
        
        return root