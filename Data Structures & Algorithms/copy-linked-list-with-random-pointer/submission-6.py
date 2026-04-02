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
        dummy = node = Node(0)
        node.next = head
        node = node.next
        node_map = {}
    
        while node:
            node_map[node] = Node(node.val)
            node = node.next
        
        node = dummy.next
        while node:
            node_map[node].next = node_map[node.next] if node.next else None
            node_map[node].random = node_map[node.random] if node.random else None
            node = node.next
        return node_map[dummy.next]