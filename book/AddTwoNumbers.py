from typing import List
from typing import Optional
import functools
from operator import add, mul

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # '''
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 전환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        '''
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        '''
        # resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))
        
        resultStr = functools.reduce(lambda x, y: 10 * x + y, a, 0) + \
            functools.reduce(lambda x, y : 10 * x + y, b, 0)
        '''    
        print(functools.reduce(add, [1, 2, 3, 4, 5]))
        print(functools.reduce(mul, [1, 2, 3, 4, 5]))
        '''
        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
    '''
if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)

    while result:
        print(result.val, end=' ')
        result = result.next
        if result:
            print('->', end=' ')