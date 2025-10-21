# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            first=list1
            second=list2
            third=last=None
            if first.val < second.val:
                third=last=first
                first=first.next
                third.next=None
            else:
                third=last=second
                second=second.next
                third.next=None
            
            while(first and second):
                if first.val < second.val:
                    last.next = first
                    last = first
                    first = first.next
                    last.next = None
                else:
                    last.next = second
                    last = second
                    second = second.next
                    last.next = None
            
            if first:
                last.next = first
            if second:
                last.next = second

            return third
        elif list1 == None and list2:
            return list2
        elif list1 and list1:
            return list1
        else:
            return
        