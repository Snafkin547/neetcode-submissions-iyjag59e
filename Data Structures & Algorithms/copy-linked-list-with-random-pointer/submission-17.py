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
        # Iter 1) Weave new Node without random after original
        # Iter 2) Point new random to original's random's next/the new random should be just after the original random
        # Iter 3) Remove original
        
        node = head
        while node:
            # Make a new copy as next
            node.next = Node(x=node.val, next = node.next)
            node = node.next.next # Move the pointer to next original
        
        node = head
        while node:
            rand = node.random
            if rand: # If no random, leave it as it is
                new_node = node.next
                new_node.random = rand.next
            node = node.next.next
        
        node = head
        res = head.next if head else None # Saving this for returned Node
        while node:
            new_node = node.next # Reference the new Copied Node
            node.next = node.next.next # Pointing next original/This works even if None
            if new_node.next: # Only if next set of node exists as this doesnt work if None
                new_node.next = new_node.next.next
            node = node.next # Move the pointer to next original
        return res

