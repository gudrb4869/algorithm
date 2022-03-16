from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, rev = head, None

        while node:
            next, node.next = node.next, rev
            node, rev = next, node

        return rev

    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
        
    def toReversedLinkedList(self, result: str) -> ListNode:
        rev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = rev
            rev = node
        
        return node
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
                # = int(''.join(map(str, a))) + int(''.join(map(str, b)))

        return self.toReversedLinkedList(str(resultStr))