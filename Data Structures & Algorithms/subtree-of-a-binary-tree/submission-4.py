# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            stack = [(p, q)]
            while stack:
                a, b = stack.pop()
                if not a and not b:
                    continue
                if a and b and a.val == b.val:
                    stack.append((a.left, b.left)) 
                    stack.append((a.right, b.right))
                else:
                    return False
            return True

        if not root and not subRoot:
            return True

        stack = []
        if root:
            stack.append(root)

        while stack:
            node = stack.pop()
            if  node.val == subRoot.val and sameTree(node, subRoot):
                return True
            if not node:
                continue
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

