# IDEA
# we can solve this problem by using greedy algorithm
# we will iterate through the array and for each position we will calculate
# the max size of jump we can make from that position in the array
# as the max from the current position and the previous max - 1
# then if we can reach the end of the array, we will return True
# in other case we will return False
# TIME COMPLEXITY
# O(N) because we iterate through the array
# SPACE COMPLEXITY

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_j = nums[0]
        if max_j == 0:
            return False

        for i in range(1, len(nums)):
            max_j = max(max_j - 1, nums[i])
            if max_j == 0 and i != len(nums) - 1:
                return False
        return True
