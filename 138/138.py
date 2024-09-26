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
# We need to modify the solution a bit, because values can be not unique. So, we need to store the indexes
# of appearance instead of values.

# IDEA3
# We can solve this problem another simple way, instead of using indexes, and instead of single values,
# we can store table of nodes for each value. So, we will have a hash table that will store the values
# and the table of nodes that have that value. because of the order of appearance, we can easily assign
# the random pointers to the copied list. by taking the first node from the table of nodes that have the
# same value as the random node, and assign it to the random pointer of the copied list.

# IDEA4
# we will store not values of nodes in the hash table, but the nodes themselves. So, we will have a hash table
# that will store the nodes of the original list, and the nodes of the copied list.




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
        if not head:
            return None
        old_to_new = {}

        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next


        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next


        return old_to_new[head]


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
