from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # this function return the sum of two linked lists in reverse order
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

    # this function return the sum of two linked lists in forward order
    def addTwoNumbersII(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # reverse the linked list
        def reverse_linked_list(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev

        l1 = reverse_linked_list(l1)
        l2 = reverse_linked_list(l2)
        return reverse_linked_list(Solution().addTwoNumbers(l1, l2))


# test
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)