# IDEA
# we can solve this problem by recursion
# if the root is None we need to return False because if there is no root there is no path
# if the root.left and root.right is None we need to check if the targetSum is equal to the root.val
# if it is return True, else return False
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
            return False
        elif root.left is None and root.right is None:
            return targetSum == root.val
        else:
            return (self.hasPathSum(root.left, targetSum - root.val) or
                    self.hasPathSum(root.right, targetSum - root.val))
