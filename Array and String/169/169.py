# IDEA
# we can solve this problem by using two main variables, one to store
# the current candidate to be majority element, and the other to store
# occurrences of the candidate, if the candidate is the same as the current
# element, we will increment the count, otherwise we will decrement the count
# if the count is zero, we will change the candidate to the current element
# TIME COMPLEXITY
# O(n), we are iterating over the array once
# SPACE COMPLEXITY
# O(1), we are using only constant space

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cd = 0
        ct = 0
        for i in range(len(nums)):
            if ct == 0:
                cd = nums[i]
                ct += 1
            elif nums[i] == cd:
                ct += 1
            else:
                ct -= 1
        return cd
