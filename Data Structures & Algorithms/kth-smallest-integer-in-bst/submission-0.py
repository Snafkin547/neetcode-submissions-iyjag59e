# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeArrays = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            nodeArrays.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        print(nodeArrays)
        return nodeArrays[k-1]