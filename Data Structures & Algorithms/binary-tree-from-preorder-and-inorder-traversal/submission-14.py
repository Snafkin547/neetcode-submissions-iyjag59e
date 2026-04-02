# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = self.predex = 0
        def dfs(lim):
            if self.index >= len(preorder):
                return None
            if inorder[self.index] == lim:
                self.index += 1
                return None
            val = preorder[self.predex]
            curr = TreeNode(val)
            self.predex += 1
            curr.left = dfs(val)
            curr.right = dfs(lim)
            return curr
        return dfs(float('inf'))