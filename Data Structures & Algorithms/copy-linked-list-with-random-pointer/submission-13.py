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
        l1 = head
        while l1:
            l2 = Node(l1.val)
            temp = l1.next
            l1.next = l2
            l1.next.next = temp
            l1 = l1.next.next
        
        l1 = head
        while l1:
            l1.next.random = l1.random.next if l1.random else None
            l1 = l1.next.next
        
        l1 = head
        res = head.next
        while l1:
            l2 = l1.next
            l1.next = l1.next.next
            if l2.next:
               l2.next = l2.next.next
            
            l1 = l1.next
            
        return res
