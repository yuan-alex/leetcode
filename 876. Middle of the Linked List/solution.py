class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        elif head.next.next is None:
            return head.next
        faster = head.next.next
        slower = head.next
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
        return slower
