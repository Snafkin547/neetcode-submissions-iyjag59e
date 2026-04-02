# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Count bottom up and if cnt == k return the Node
        if not root:
            return -1
        cnt = 0
        st = []
        curr = root
        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            cnt += 1
            if cnt == k:
                return curr.val
            curr = curr.right
        return -1
