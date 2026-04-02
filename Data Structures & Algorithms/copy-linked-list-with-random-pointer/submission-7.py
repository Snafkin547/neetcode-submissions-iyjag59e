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
        if not head:
            return
        
        node = head
        node_map = defaultdict(lambda: Node(0))
        node_map[None] = None
    
        while node:
            node_map[node].val = node.val
            node_map[node].next = node_map[node.next]
            node_map[node].random = node_map[node.random]
            node = node.next
        return node_map[head]