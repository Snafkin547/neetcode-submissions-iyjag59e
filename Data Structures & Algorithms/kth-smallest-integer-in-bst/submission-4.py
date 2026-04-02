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
        visited = set([None, root])
        cnt = 0
        st = [root]
        while st:
            node = st[-1]
            if node.left not in visited:
                st.append(node.left)
                visited.add(node.left)
                
            else:
                node = st.pop()
                cnt += 1
                if cnt == k:
                    return node.val
                if node.right not in visited:
                   st.append(node.right)
                   visited.add(node.right)
        return -1
