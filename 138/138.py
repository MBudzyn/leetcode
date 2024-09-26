# IDEA
# We can solve this problem by using hash table, and iterate two times through the list.
# First time, we will create a copy of the list, but without random pointers, and at the
# same time we will create a hash table that will store the values and the pointers to the nodes
# of the copied list. Second time, we will iterate through the list, and we will assign the random
# pointers to the copied list by using the hash table.
# TIME COMPLEXITY
# O(N) because we iterate two times through the list
# SPACE COMPLEXITY
# O(N) because we create a hash table that will store the values and the pointers to the nodes
# of the copied list. Also, we create a copy of the list.

# IDEA2
# We need to modify the solution a bit, becouse values can be not unique. So, we need to store the indexes
# of appearance instead of values.


from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        cp = self
        while cp:
            print("val: ", cp.val, "random: ", cp.random.val if cp.random else None)
            cp = cp.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dct = {}
        org_head = head
        res_head = Node(head.val) if head else None
        copy_head = res_head
        while head:
            copy_head.next = Node(head.next.val) if head.next else None
            dct[copy_head.val] = copy_head
            head = head.next
            copy_head = copy_head.next

        while org_head:
            dct[org_head.val].random = dct[org_head.random.val] if org_head.random else None
            org_head = org_head.next

        return res_head


s = Solution()
head = Node(7)
head.next = Node(13)
head.next.random = head
head.next.next = Node(11)
head.next.next.random = head.next
head.next.next.next = Node(10)
head.next.next.next.random = head.next.next
head.next.next.next.next = Node(1)

head.__str__()
print()
s.copyRandomList(head).__str__()
