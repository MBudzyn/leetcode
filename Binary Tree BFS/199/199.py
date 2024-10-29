# IDEA
# we can solve this problem by iterating through the tree using stack (BFS)
# and to the result we can add the value of the node in the last position of
# actual layer.
# The time complexity is O(n) where n is the number of nodes in the tree
# The space complexity is O(n) where n is the number of nodes in the tree
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        stack = [root]
        while stack:
            new_stack = []
            result.append(stack[-1].val)
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return result
