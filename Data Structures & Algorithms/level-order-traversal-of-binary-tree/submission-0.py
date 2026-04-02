# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # WFS
        # create res array and current array
        current, res = [], []
        # append current node to current array
        current.append(root)
        while len(current) > 0:
            # create vals, temp arrays
            vals, temp = [], []
            # for loop current, append its value to vals array, and append children, if exist, to temp array
            for curr in current:
                vals.append(curr.val)
                left, right = curr.left, curr.right
                if left:
                    temp.append(left)
                if right:
                    temp.append(right)
            current = temp
            res.append(vals)
        return res