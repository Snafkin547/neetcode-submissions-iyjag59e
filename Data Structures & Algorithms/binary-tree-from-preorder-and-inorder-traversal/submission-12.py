# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inO = {val:idx for idx, val in enumerate(inorder)}
        self.idx = 0
        def dfs(l, r):
            if l > r:
                return
            val = preorder[self.idx]
            curr = TreeNode(val)
            self.idx += 1
            m = inO[val]
            curr.left, curr.right = dfs(l, m-1), dfs(m+1, r)
            return curr
        return dfs(0, len(preorder)-1)