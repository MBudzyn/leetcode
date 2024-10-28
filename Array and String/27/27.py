# IDEA
# we will use the simple idea to pop elements equal to value
# and then return the length of the array
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ct = 0
        indeksy = [i for i in range(len(nums)) if nums[i] == val]
        for i in indeksy:
            nums.pop(i-ct)
            ct += 1
        return len(nums)