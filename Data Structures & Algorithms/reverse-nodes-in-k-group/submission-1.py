# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, n):
            while node and n:
                node = node.next
                n -= 1
            return node
        
        groupPrev = dummy = ListNode(0, head)
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            
            curr = groupPrev.next #The beginning node of the curr block
            prev = groupNext = kth.next # Holding the start of the next block, which curr shall points to
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next # The tail of the current block/one node preceding next blcok
            groupPrev.next = kth # The preceding node to the current block shall point to the updated head of the current blcok
            groupPrev = temp # The subsequent iteration shall start from the one node preceding the next block
        return dummy.next
            
            
