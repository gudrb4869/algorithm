# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    lst = []

    if not head:
        return True

    while head:
        lst.append(head.val)
        head = head.next

    while len(lst) > 1:
        if lst.pop(0) != lst.pop():
            return False

    return True

print(isPalindrome(ListNode(1,ListNode(2))))
print(isPalindrome(ListNode(1,ListNode(2,ListNode(2, ListNode(1))))))