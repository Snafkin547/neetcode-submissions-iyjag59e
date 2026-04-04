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
        
        mp ={None:None} # v : Node
        node = head
        prev = None
        while node:            
            mp[node] = Node(x = node.val)
            if prev:
                prev.next = mp[node]
            prev = mp[node]
            node = node.next
        
        node = head
        while node:
            mp[node].random = mp[node.random]
            node = node.next
        return mp[head]
        