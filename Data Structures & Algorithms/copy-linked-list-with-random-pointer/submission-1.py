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
        dummy = Node(0)
        curr = dummy
        runner = head  

        nodeMap ={None: None} # Maps original:new

        while runner:
            # Copy just val and original random
            curr.next = Node(runner.val, None, runner.random)
            curr = curr.next

            # Map old to new
            nodeMap[runner] = curr
            runner = runner.next

        # Link random of new node to node at the idx of new LL
        curr = dummy.next
        while curr:
            curr.random = nodeMap[curr.random] 
            curr = curr.next
        return nodeMap[head]