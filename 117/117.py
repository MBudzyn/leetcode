# IDEA
# to add next pointer to each node, we can iterate through the tree by layers using stack
# and for every node we will add the next pointer to the next node in the stack
# and all time we will append the left and right child to the new stack and at the end
# we will swap the stacks
# Time complexity: O(n)
# Space complexity: O(n) in worst case we will store all nodes of the last layer in the stack
# which is n/2 nodes in the worst case


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        head = root
        new_stack = []

        while stack:
            for i in range(len(stack)):
                if i + 1 < len(stack):
                    stack[i].next = stack[i + 1]
                if stack[i].left:
                    new_stack.append(stack[i].left)
                if stack[i].right:
                    new_stack.append(stack[i].right)
            stack = new_stack
            new_stack = []
        return head

