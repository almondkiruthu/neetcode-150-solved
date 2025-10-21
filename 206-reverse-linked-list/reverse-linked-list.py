# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reversing a linked list using the 3-sliding pointers technique.
        third=second=first=None
        if head:
            first = head
            while first != None:
                third = second
                second = first
                first = first.next
                second.next = third
            head = second
            return head
        else:
            return
        