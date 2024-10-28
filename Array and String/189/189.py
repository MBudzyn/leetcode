# IDEA
# we can solve this problem by using simple operations on list to get the
# first and second part of the list and swap them to get the desired output
# TIME COMPLEXITY
# The time complexity is O(n) as we are iterating through the list only once
# SPACE COMPLEXITY
# The space complexity is O(1) as we are not using any extra space

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
