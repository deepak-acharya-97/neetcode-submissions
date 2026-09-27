"""
https://neetcode.io/problems/merge-two-sorted-linked-lists
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        temp = ListNode()
        result = temp

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = ListNode(temp1.val)
                temp = temp.next
                temp1 = temp1.next
            else:
                temp.next = ListNode(temp2.val)
                temp = temp.next
                temp2 = temp2.next

        while temp1:
            temp.next = ListNode(temp1.val)
            temp = temp.next
            temp1 = temp1.next

        while temp2:
            temp.next = ListNode(temp2.val)
            temp = temp.next
            temp2 = temp2.next

        return result.next
