# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, rev = head, None

        while node:
            # rev, rev.next, node = node, rev, node.next
            next, node.next = node.next, rev
            node, rev = next, node

        return rev