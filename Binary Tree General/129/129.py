# IDEA
# we can solve this problem by using recursion
# if the node is the leaf, (node.left is None and node.right is None) then we return node.value
# otherwise, we actualize the value of the sons which are not None and return sum of the recursive call
# on the left and right sons
# TIME COMPLEXITY
# O(n) -- we visit every node once
# SPACE COMPLEXITY
# O(h) -- h is the height of the tree, the maximum depth of the recursion stack which in worst case is O(n)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.right is None and root.left is None:
            return root.val
        else:
            if root.right is not None:
                root.right.val = root.val * 10 + root.right.val
            if root.left is not None:
                root.left.val = root.val * 10 + root.left.val
            return (self.sumNumbers(root.right) +
                    self.sumNumbers(root.left))
