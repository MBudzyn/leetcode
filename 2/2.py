# IDEA
# problem solution is very simple, we will create empty list and iterate through the input lists
# at the same time and append sum of the elements % 10 + carry to the result list and update carry
# then we will repeat the process until we reach the end of one of the one or both lists
# then we need to check if one lists is not empty and add the rest of the elements to the result list
# then we need to check if carry is greater than 0 and add it to the result list
# at the end we need to return the head of the result list
# TIME COMPLEXITY
# The time complexity is O(n) because we only need to iterate the lists once
# SPACE COMPLEXITY
# The space complexity is O(n) because we need to store the result list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = 0
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            res.val = sum % 10
            l1 = l1.next
            l2 = l2.next
            if l1 is not None and l2 is not None:
                res.next = ListNode()
                res = res.next

        if l1 is not None:
            while l1 is not None:
                sum = l1.val + carry
                carry = sum // 10
                res.next = ListNode(sum % 10)
                res = res.next
                l1 = l1.next

        if l2 is not None:
            while l2 is not None:
                sum = l2.val + carry
                carry = sum // 10
                res.next = ListNode(sum % 10)
                res = res.next
                l2 = l2.next

        if carry > 0:
            res.next = ListNode(carry)

        return head