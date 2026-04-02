# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helperSubtree(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            return helperSubtree(node1.left, node2.left) and helperSubtree(node1.right, node2.right)

        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
               if helperSubtree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False