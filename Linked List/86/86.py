# IDEA
# we will partition the linked list into two parts, one that will store
# elements less than x and the other that will store elements greater
# or equal to x. We will then merge the two lists to get the desired output
# TIME COMPLEXITY
# The time complexity is O(n) as we are iterating through the list only once
# SPACE COMPLEXITY
# The space complexity is O(1) as we are not using any extra space

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = None
        less = None
        greater_head = None
        less_head = None
        while head:
            if head.val < x:
                if less:
                    less.next = head
                    less = less.next
                else:
                    less = head
                    less_head = less
            else:
                if greater:
                    greater.next = head
                    greater = greater.next
                else:
                    greater = head
                    greater_head = greater
            head = head.next
        if greater:
            greater.next = None
            if less:
                less.next = greater_head
                return less_head
            else:
                return greater_head
        elif less:
            less.next = None
            return less_head

        return None
