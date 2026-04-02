# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        flag = True
        while queue:
            cur = queue.pop()
            if cur:
                if cur.val == subRoot.val:
                    first = [cur]
                    second = [subRoot]
                    while first and second:
                        f = first.pop()
                        s = second.pop()
                        if not f and not s:
                            continue
                        elif f and s and f.val == s.val:
                            first.append(f.left)
                            first.append(f.right)
                            second.append(s.left)
                            second.append(s.right)
                        else:
                            flag = False
                            break
                    if flag and not first and not second:
                        return True
                    else:
                        flag = True
                
                queue.append(cur.left)
                queue.append(cur.right)
        return False