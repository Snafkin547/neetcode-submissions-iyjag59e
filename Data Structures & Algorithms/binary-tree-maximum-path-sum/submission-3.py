# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return float('-inf'), float('-inf')
            
            # sofar best: left only, right only, inclusive
            # inclusive best: root only, left/right + root, or all
            
            left_sofar, left_incl = helper(node.left)
            right_sofar, right_incl = helper(node.right)

            sofar = node.val
            sofar += left_incl if left_incl > 0 else 0
            sofar += right_incl if right_incl > 0 else 0
            sofar = max(left_sofar, right_sofar, sofar)

            lr = max(left_incl, right_incl, 0) # Upper layer can aggregate only one or fewer branche
            incl = node.val + lr
            return sofar, incl
            
        sofar, incl = helper(root)
        return max(sofar, incl)
'''
[5,4,8,11,null,13,4,7,2,null,null,null,1]
         5,
        4,  8,
    11,null,13,4,
 7,2,null,null,null,1]
'''