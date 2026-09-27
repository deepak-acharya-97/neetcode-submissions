"""
https://neetcode.io/problems/add-two-numbers
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        dummy = result

        while l1 or l2 or carry:
            op1 = 0 if not l1 else l1.val
            op2 = 0 if not l2 else l2.val

            answer = op1 + op2 + carry
            print(answer)

            result.next = ListNode(answer%10)
            result = result.next
            carry = answer // 10

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
