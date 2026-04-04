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
        
        mp = defaultdict(lambda: Node(0))
        mp[None] = None
        node = head
        while node:
            mp[node].val = node.val
            mp[node].next = mp[node.next]
            mp[node].random = mp[node.random]
            node = node.next
        return mp[head]
        