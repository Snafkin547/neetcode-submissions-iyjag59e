# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            return self.divide(lists, 0, len(lists) - 1)
        else:
            return None

    def divide(self, lists, l, r):
        if l > r:
            return None
        elif l == r:
            return lists[l]
        
        mid = l + (r - l)//2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)
        return self.concur(left, right)
    
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
