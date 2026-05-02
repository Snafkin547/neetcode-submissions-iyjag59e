# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minH = [] #(val, node)
        for node in lists:
            if node:
                heapq.heappush(minH, NodeWrapper(node))
        
        dummy = head = ListNode()
        while minH:
            nW = heapq.heappop(minH)
            head.next = nW.node
            head = head.next
            
            if nW.node.next:
                heapq.heappush(minH, NodeWrapper(nW.node.next))

        return dummy.next
            
                