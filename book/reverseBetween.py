from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next
        
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
        
if __name__ == "__main__":
    solution = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    result = solution.reverseBetween(l, 2, 5)

    while result:
        print(result.val,end=' ')
        result = result.next