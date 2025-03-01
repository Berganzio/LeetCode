from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a head node
        head = ListNode()
        # create a current to the head node
        current = head
        # iterate through the two lists
        while list1 and list2:
            # if the value of list1 is less than list2
            if list1.val < list2.val:
                # assign the value of list1 to the current
                current.next = list1
                # move list1 to the next node
                list1 = list1.next
            else:
                # assign the value of list2 to the current
                current.next = list2
                # move list2 to the next node
                list2 = list2.next
            # move the current to the next node
            current = current.next
        # if there are remaining nodes in list1
        if list1:
            # assign the remaining nodes of list1 to the current
            current.next = list1
        # if there are remaining nodes in list2
        if list2:
            # assign the remaining nodes of list2 to the current
            current.next = list2
        # return the next node of the head node
        return head.next

# test
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = Solution().mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
print()