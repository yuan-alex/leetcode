# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def listToBST(self, lst):
        if len(lst) > 0:
            mid = len(lst) // 2
            new = TreeNode(
                lst[mid], self.listToBST(lst[:mid]), self.listToBST(lst[mid + 1 :])
            )
            return new
        return None

    def toList(self, head):
        lst = []
        pointer = head
        while pointer:
            lst.append(pointer.val)
            pointer = pointer.next
        return lst

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.listToBST(self.toList(head))