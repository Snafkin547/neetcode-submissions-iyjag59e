# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        n = k = len(lists)
        while k > 1:
            # decrement n if end of each list appended
            temp = None
            for i in range(n):
                if lists[i] and (not temp or lists[i].val < temp.val):
                    temp = lists[i]
                    idx = i
            head.next = temp
            head = head.next
            lists[idx] = lists[idx].next
            if not lists[idx]:
                k -= 1

        for i in range(n):
            if lists[i]:
                head.next = lists[i]
                break
        return res.next
        