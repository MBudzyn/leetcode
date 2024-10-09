# IDEA
# we will iterate over the tree using stack, and for every node in the stack we will
# swap the left and right children, then we will append the left child and right child
# to the stack if they are not None
# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        if head is None:
            return None
        stack = [root]
        while stack:
            actual = stack.pop(0)
            tmp_l = actual.left
            actual.left = actual.right
            actual.right = tmp_l
            if actual.left:
                stack.append(actual.left)
            if actual.right:
                stack.append(actual.right)
        return head
