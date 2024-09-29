# IDEA
# we can solve this problem by simply deleting the duplicates
# iterating through the list from the second element to the end
# if the current element is equal to the previous element, we delete it
# we return the length of the list after deleting the duplicates
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
