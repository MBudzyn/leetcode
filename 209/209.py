# IDEA
# we can use two pointers to solve this problem
# we need to set two pointers, one on the left and one on the right
# then we can move right pointer to the right and check if the sum of
# the subarray is greater or equal to the target number
# if it is, we can move left pointer to the right minimizing the sum near to the target number
# but still greater or equal to the target number and actualize the minimum size of the subarray
# TIME COMPLEXITY
# the time complexity is O(n) because we only need to iterate the array once
# SPACE COMPLEXITY
# the space complexity is O(1) because we only need to use two pointers to solve this problem
# and constant number of variables



class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum = 0
        left = 0
        right = 0
        min_size = float("inf")
        while right < len(nums):
            sum += nums[right]
            right += 1
            if sum >= target:
                while sum - nums[left] >= target:
                    sum -= nums[left]
                    left +=1
                if min_size > right - left:
                    min_size = right - left
        if sum < target:
            return 0
        else:
            return min_size
