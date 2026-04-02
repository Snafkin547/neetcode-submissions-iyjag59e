# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 or l2:
            curr = carry
            if l1:
                curr +=l1.val
                l1 = l1.next
            if l2:
                curr +=l2.val
                l2 = l2.next
            carry = curr//10
            curr = curr%10
            head.next = ListNode(curr)
            head = head.next
        if carry != 0:
            head.next = ListNode(carry)
        return dummy.next
