# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inO = {val:idx for idx, val in enumerate(inorder)}
        n = len(preorder)
        def dfs(l, r, idx):
            if l > r or idx >= n:
                return
            val = preorder[idx]
            curr = TreeNode(val)
            
            curr.left = dfs(l, inO[val] - 1, idx + 1)
            curr.right = dfs(inO[val] + 1, r, idx + inO[val] - l + 1)

            return curr

        return dfs(0, n - 1, 0)