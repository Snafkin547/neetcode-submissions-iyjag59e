# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, node):
        res = []

        st = [node]

        while st:
            curr = st.pop()
            if not curr:
                res.append("$#")
                continue
            res.append(f"${curr.val}")
            st.append(curr.left)
            st.append(curr.right)
        return "".join(res)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        serial_root = self.serialize(root)
        serial_subroot = self.serialize(subRoot)
        print(serial_root, serial_subroot)
        return serial_subroot in serial_root
