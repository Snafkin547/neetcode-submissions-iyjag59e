# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)} # Max Height, Max Diameter
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftH, leftD = mp[node.left]
                rightH, rightD = mp[node.right]
                mp[node] = (1 + max(leftH, rightH), max(leftH + rightH, leftD, rightD))
        return mp[root][1]