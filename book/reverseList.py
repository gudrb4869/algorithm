class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        def reverse(node: ListNode, prev:ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)
        '''
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
        
if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseList(head)

    while result:
        print(result.val, end='->')
        result = result.next

    print('NULL')