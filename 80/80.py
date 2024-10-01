# IDEA
# because we can store whatever we want at the end of the array,
# we will be simply skipping the elements that have more than 2 occurrences
# and rest of the elements will be moved to the left of the array, on
# the first skipped place, then we will actualize the index to move the elements
# to the left of the array, and we will return the index of the last "to_insert"

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ct = 0
        duplicate_ct = 1
        to_insert = -1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                duplicate_ct += 1
                if duplicate_ct == 3 and to_insert == -1:
                    to_insert = i
            else:
                duplicate_ct = 1

            if to_insert != -1 and duplicate_ct <= 2:
                nums[to_insert] = nums[i]
                to_insert += 1
                ct += 1

        return to_insert if to_insert != -1 else len(nums)
