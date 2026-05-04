# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append("¥")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return '#'.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self,data: str) -> Optional[TreeNode]:
        # while q or first
        # count length and work only on thise count
        # append if not none
        i = 0
        dummy = TreeNode()
        q = deque([dummy])
        n = len(data)
        while q:
            size = len(q)
            while size:
                parent = q.popleft()
                it = 1 if i == 0 else 2
                for isRight in range(it):
                    r = i
                    while r < n and data[r] != '#':
                        r += 1
                    
                    val = data[i:r]
                    
                    if val == '¥':
                        i = r + 1
                        continue
                    
                    node = TreeNode(val = int(val))
                    if isRight:
                        parent.right = node
                    else:
                        parent.left = node
                    q.append(node)
                    i = r + 1
                size -= 1
        return dummy.left
        



