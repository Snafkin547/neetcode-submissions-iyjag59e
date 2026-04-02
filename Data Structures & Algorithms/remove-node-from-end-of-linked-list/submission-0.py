# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        runner = head
        for i in range(n):
            runner = runner.next
        
        ans = res
        while runner:
            res = res.next
            runner = runner.next
        
        res.next = res.next.next
        return ans.next
        

        
