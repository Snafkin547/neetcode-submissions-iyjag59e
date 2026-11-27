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

        # BFS: Swap 
        # push left and right if not none
        q = deque([root])
        while q:
            node = q.popleft()
            l = node.left
            r = node.right
            node.left, node.right = r, l
            if l:
                q.append(l)
            if r:
                q.append(r)
        
        return root