# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index, self.predex = 0, 0
        def dfs(limit):
            if self.index  >= len(inorder):
                return 
            if inorder[self.index] == limit:
                self.index += 1
                return

            val = preorder[self.predex]
            curr = TreeNode(val)
            self.predex += 1

            curr.left = dfs(val)
            curr.right = dfs(limit)
            return curr

        return dfs(float('inf'))