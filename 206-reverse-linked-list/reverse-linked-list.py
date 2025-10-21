# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last=middle=first=None
        if head:
            first = head
        else:
            return
        while first != None:
            last = middle
            middle = first
            first = first.next
            middle.next = last
        head = middle
        return head
    
        