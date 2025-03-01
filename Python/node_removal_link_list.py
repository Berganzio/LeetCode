from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next   


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, both pointing to the head of the list
        first, second = head, head
        # Move the first pointer n steps ahead
        # If the first pointer becomes None, it means the node to be removed is the head node
        for _ in range(n):
            first = first.next

            if not first:
                return head.next
        # Move both pointers one step at a time until the first pointer reaches the end of the list
        # The second pointer will be at the node just before the nth node from the end
        while first.next:
            first = first.next
            second = second.next
        # Remove the nth element by updating the next pointer of the second pointer
        second.next = second.next.next
        return head


# test
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().removeNthFromEnd(head, 2))