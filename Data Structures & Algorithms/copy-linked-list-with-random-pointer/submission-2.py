"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head  
        nodeMap ={None: None} # Maps original:new

        while curr:
            # Copy just val and original random
            copy = Node(curr.val)
            nodeMap[curr] = copy
            curr = curr.next

        # Link random of new node to node at the idx of new LL
        curr = head  
        while curr:
            copy = nodeMap[curr]
            copy.next = nodeMap[curr.next]
            copy.random = nodeMap[curr.random] 
            curr = curr.next
        return nodeMap[head]