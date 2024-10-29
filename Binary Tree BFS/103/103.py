# IDEA
# we can solve this problem by iterating through the tree using stack (BFS)
# and depending on actual case we will add the lvl in normal order or reversed
# The time complexity is O(n) where n is the number of nodes in the tree
# The space complexity is O(n) where n is the number of nodes in the tree
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        res = []
        case = 1
        if not root:
            return []

        while stack:
            new_stack = []
            tmp_lvl = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
                tmp_lvl.append(node.val)
            if case == 0:
                res.append(tmp_lvl[::-1])
            else:
                res.append(tmp_lvl)
            case = 1 - case
            stack = new_stack

        return res

