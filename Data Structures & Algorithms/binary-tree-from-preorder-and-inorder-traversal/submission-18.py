# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        predex = index = 0
        head = TreeNode(None)
        curr = head
        n = len(preorder)
        # Preorder : root - leftTree - rightTree
        # Inorder : leftTree - root - rightTree
        # Postorder : leftTree - rightTree - root

        while predex < n and index < n:
            # Create a right node
            curr.right = TreeNode(preorder[predex], right = curr.right) # This curr.right preserves successor/subroot above
            curr = curr.right
            predex += 1
            while predex < n and index < n and curr.val != inorder[index]:
                # Create all left nodes from the sub-root till you hit the end of it(first index of inorder in curr iteration)
                curr.left = TreeNode(preorder[predex], right = curr)
                curr = curr.left
                predex += 1
            index += 1
            while index < n and curr.right and curr.right.val == inorder[index]:
                # Move up till you hit a node with a yet-created right subtree
                # This works because inorder separates left and right subtree by a root
                prev = curr.right
                curr.right = None
                curr = prev
                index += 1
        return head.right

