# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Naive slice by k
        # Use head and Tail to avoid full traversal
        q = []
        prev = None
        tail = curr = head

        size = 0
        while curr:
            curr = curr.next
            size += 1

        # Slice into each k length
        curr = head
        while curr and k <= size:
            n = k
            while curr and n:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                n -= 1

            q.append((prev, tail))
            prev = None
            tail = curr
            size -= k

        if curr:
            q.append((curr, None))

        res = dummy = ListNode()

        for i in range(len(q)):
            head, tail = q[i]
            dummy.next = head
            dummy = tail
        return res.next