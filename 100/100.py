# IDEA
# Trees are identical if they have the same structure and the same node values at each position.
# We can use the recursive function to check if the trees are identical.
# if in any node the values are different, we can return False
# if we reach the end of the tree, we can return True
# TIME COMPLEXITY
# O(n) because we need to visit every node in the tree
# SPACE COMPLEXITY
# O(n) because of the recursion stack

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))

