# IDEA
# we can solve this problem by using two pointers,
# one pointer will by in 0 position, and the other we will move two n position
# then we will move two pointers at the same time, until the second pointer reaches the end
# then we will remove the node that is the next node of the first pointer
# TIME COMPLEXITY
# O(N) because we iterate through the list
# SPACE COMPLEXITY
# O(1) because we don't use any extra space

# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        original_head = head
        first = head

        for i in range(n):
            head = head.next
        second = head

        if not second:
            return first.next

        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next

        return original_head





