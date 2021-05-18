# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode(None)
        outputPointer = output
        carry = 0
        pointer1, pointer2 = l1, l2
        while pointer1 or pointer2:
            if pointer1 and pointer2:
                new = pointer1.val + pointer2.val
            elif pointer1:
                new = pointer1.val
            elif pointer2:
                new = pointer2.val
            new += carry
            if new >= 10:
                carry = int(new / 10)
                new -= 10
            else:
                carry = 0
            outputPointer.next = ListNode(new)
            outputPointer = outputPointer.next
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
        if carry > 0:
            outputPointer.next = ListNode(carry)
        return output.next