# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        pointer = head
        while pointer:
            actual_next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = actual_next
        return prev