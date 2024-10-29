# IDEA
# at the beginning we will create a help function that will parse the tmp array
# to correct format, then we will use simple greedy algorithm that will
# check if the next element have value, exactly previous + 1 and if not
# we will call pom function to parse correct fragment of the array

from typing import List


def str_from_arr(arr: List[int]) -> str:
    if len(arr) == 1:
        return str(arr[0])
    else:
        return str(arr[0]) + "->" + str(arr[-1])


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        last_ind = 0
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                res.append(str_from_arr(nums[last_ind:i + 1]))
                last_ind = i + 1
        if last_ind < len(nums):
            res.append(str_from_arr(nums[last_ind:]))
        return res
