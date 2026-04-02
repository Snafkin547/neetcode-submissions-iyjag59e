# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        node = ListNode(0)
        node.next = list1
        temp = None
        while list1 and list2:
            if list1.val > list2.val:
                temp = list1.val
                nextNode = list1.next
                list1.val = list2.val
                list1.next = ListNode(temp)
                list1.next.next = nextNode
                list1 = list1.next
                list2 = list2.next
            else:
                if list1.next:
                    list1 = list1.next
                else:
                    break
        if list2:
           list1.next = list2
        
        return node.next