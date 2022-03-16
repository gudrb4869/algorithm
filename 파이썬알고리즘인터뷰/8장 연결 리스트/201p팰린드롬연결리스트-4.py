# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev

    return True

print(isPalindrome(ListNode(1,ListNode(2))))
print(isPalindrome(ListNode(1,ListNode(2,ListNode(2, ListNode(1))))))