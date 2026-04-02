# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preKey, start, end):
            if start > end  or preKey>=len(preorder):
                return
            
            currNode = TreeNode(preorder[preKey])
            
            # Search for preKey in inorder
            i = 0
            while i<=end and preorder[preKey] != inorder[start + i]:
                i += 1
            
            # Give preKey, Slice inorder just before: start(0) and end(i - 1) to left recursion
            if i > 0: # Left subtree exists
                currNode.left = dfs(preKey + 1, start, start + i - 1)

            # Make preKey += i (Cut off all Left Node)
            preKey += (i + 1)
            # Give preKey start(i) and end(len(inorder) - 1) to left recursion
            currNode.right = dfs(preKey, start + i + 1, end)
            return currNode

        return dfs(0, 0, len(inorder) - 1)