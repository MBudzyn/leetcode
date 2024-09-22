# IDEA
# We can use two pointers to solve this problem
# We need to set two pointers, one on the left and one on the right of the array
# Then we can calculate the area between those two pointers and actualize the maximum area
# Then we can move the pointer with the smaller height to the right or left depending on the height
# and actualize the maximum area if the new area is greater than the biggest one
# TIME COMPLEXITY
# The time complexity is O(n) because we only need to iterate the array once
# SPACE COMPLEXITY
# The space complexity is O(1) because we only need to use two pointers to solve this problem
# and constant number of variables

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left != right:
            res = max(res, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

