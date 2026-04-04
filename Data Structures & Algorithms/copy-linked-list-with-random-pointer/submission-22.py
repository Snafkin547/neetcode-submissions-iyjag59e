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
            if not node in mp:
                mp[node] = Node(x = node.val)
            
            # Create a new copy for random if not present, else reference existing
            if node.random in mp:
                mp[node].random = mp[node.random]
            else:
                mp[node].random = mp[node.random] = Node(x = node.random.val)
                
            if prev: # Skip first node
                prev.next = mp[node]

            prev = mp[node]
            node = node.next        
        return mp[head]
        