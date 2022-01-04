from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return head
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head

if __name__ == "__main__":
    solution = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.oddEvenList(l)

    while result:
        print(result.val, end=' ')
        result = result.next