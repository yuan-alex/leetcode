# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        
        pointer = head
        list_length = 0
        while pointer:
            list_length += 1
            pointer = pointer.next
        
        pointer = dummy
        for i in range(list_length - n):
            pointer = pointer.next
        if pointer.next and pointer.next.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = None
        return dummy.next
