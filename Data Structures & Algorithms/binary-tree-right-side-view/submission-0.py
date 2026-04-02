# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # compare lengths of returned arrays from left and right 
        # prioritize nodes from right and create 
        if not root:
            return []
        lArray = self.rightSideView(root.left)
        rArray = self.rightSideView(root.right)
        res = [root.val]
        i = 0
        while i <len(rArray):
            res.append(rArray[i])
            i+=1
        while i <len(lArray):
            res.append(lArray[i])
            i+=1
        return res
            

        