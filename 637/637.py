# IDEA
# we can iterate through the tree using stack (BFS)
# and for each lvl calculate the average value of the nodes
# TIME COMPLEXITY
# O(n) where n is the number of nodes in the tree
# SPACE COMPLEXITY
# O(n) where n is the number of nodes in the tree

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            new_stack = []
            tmp = 0
            for node in stack:
                tmp += node.val
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            res.append(tmp / len(stack))
            stack = new_stack
        return res
