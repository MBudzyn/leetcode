# IDEA
# we will iterate through the tree using the stack, and we will be adding each level of
# values to the result list
# TIME COMPLEXITY
# O(n) -- we visit every node once
# SPACE COMPLEXITY
# O(n) in the worst case, when we store all the nodes of the last layer in the stack
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        stack = [root]
        if root is None:
            return []
        while stack:
            value_tmp = []
            new_stack = []
            for node in stack:
                value_tmp.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            result.append(value_tmp)
            stack = new_stack
        return result
