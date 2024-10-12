# IDEA
# to add next pointer to each node, we can iterate through the tree by layers using stack
# and for every node we will add the next pointer to the next node in the stack
# and all time we will append the left and right child to the new stack and at the end
# we will swap the stacks
# Time complexity: O(n)
# Space complexity: O(n) in worst case we will store all nodes of the last layer in the stack
# which is n/2 nodes in the worst case



