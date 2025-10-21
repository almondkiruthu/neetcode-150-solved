# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            if head.next == None:
                return False
            # Give the two pointers an equal start.
            slow=fast=head

            #The condition is while our fast.next.next is not null which we check by
            # fast != None condition and also check we can move forward with fast.
            while fast and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
        else:
            return