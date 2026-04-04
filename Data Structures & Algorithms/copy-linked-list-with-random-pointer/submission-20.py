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
        # Copy the current node and return it at the end, so its previous can point to it
        # Keep all nodes in a Hashmap, v: Node
        # Recurse before working on a random pointer
        mp ={None:None} # v : Node
        def helper(node):
            if not node:
                return
            
            # Memorize the node immediately, so that lower layers can reference it for rand
            mp[node] = Node(x = node.val)
            mp[node].next = helper(node.next)
                        
            # Add random only if it exists, otherwise leave it as None
            if node.random:
                mp[node].random = mp[node.random]
            return mp[node]
        return helper(head)