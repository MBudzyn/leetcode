# IDEA
# we can solve this problem by recursion
# if the root is None the return True if the targetSum is 0
# else return recursion (root.left, targetSum - root.val) or recursion(root.right, targetSum - root.val)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return targetSum == 0
        else:
            return (self.hasPathSum(root.left, targetSum - root.val) or
                    self.hasPathSum(root.right, targetSum - root.val))
