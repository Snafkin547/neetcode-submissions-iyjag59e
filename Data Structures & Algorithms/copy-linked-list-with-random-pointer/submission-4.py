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
        # Link two 
        first = head
        while first:
            second = Node(first.val)
            second.next = first.random
            first.random = second
            first = first.next
        
        newHead = head.random

        # Copy random
        first = head
        while first:
            second = first.random
            second.random = second.next.random if second.next else None
            first = first.next

        # Remove first
        first = head
        while first:
            second = first.random
            first.random = second.next
            second.next = first.next.random if first.next else None
            first = first.next
        return newHead