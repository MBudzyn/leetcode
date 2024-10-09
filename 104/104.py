# IDEA
# the max depth of the binary tree is the maximum depth of the left or right subtree + 1
# we can create a recursive function that will return the maximum depth of the tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


