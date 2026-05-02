# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        q = deque(lists)
        while len(q) > 1:
            left = q.popleft()
            right = q.popleft()
            curr = self.concur(left, right)
            q.append(curr)
        return q[0]
    
    def concur(self, left, right):
        dummy = head = ListNode()
        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        if left:
            dummy.next = left
        else:
            dummy.next = right
        return head.next
