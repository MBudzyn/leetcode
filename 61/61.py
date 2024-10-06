# IDEA
# in first iteration, we need to count number of elements in the linked list
# ten we need to actualize the value of k to k % n (n is the number of elements in the linked list)
# then we need to find the element that is n - k - 1, and correctly merge two parts of the linked list
# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        ct = 1
        actual = head

        while actual.next is not None:
            ct += 1
            actual = actual.next

        last = actual
        k = k % ct

        if k == 0:
            return head

        actual = head

        for i in range(ct - k - 1):
            actual = actual.next

        res_head = actual.next
        actual.next = None
        last.next = head
        return res_head
