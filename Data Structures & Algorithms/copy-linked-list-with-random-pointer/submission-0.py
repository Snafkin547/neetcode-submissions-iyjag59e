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
        reserve = head

        nodeMap ={} # Maps original:new
        randomMap = {} # Old Node: list of new Nodes requiring new radom node

        while head:
            # Copy just vals
            curr.next = Node(head.val)
            curr = curr.next

            # Map old to new
            nodeMap[head] = curr

            # Store required index in map
            lis = randomMap.get(head.random, [])
            lis.append(curr)
            randomMap[head.random] = lis

            head = head.next

        # Link random of new node to node at the idx of new LL
        while reserve:
            newNode = nodeMap[reserve]
            lis = randomMap.get(reserve, [])
            for l in lis:
                l.random = newNode
            reserve = reserve.next

        return dummy.next