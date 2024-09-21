# IDEA
# because the array is sorted, we can use two pointers to solve this problem
# in the beginning, we need to set two pointers, neer by half of the target number
# one on the left and one on the right, then we can compare the sum of those two numbers
# and if the sum is greater than the target number, we can move the right pointer to the left
# and if the sum is less than the target number, we can move the left pointer to the right
# and if the sum is equal to the target number, we can return the index of those two numbers
# TIME COMPLEXITY
# the time complexity is O(n) because we only need to iterate the array once
# we could use the binary search to find start pointers, but it will not change the O(n) time complexity
# SPACE COMPLEXITY
# the space complexity is O(1) because we only need to use two pointers to solve this problem

def find_start_pointers(numbers: list[int], target: int) -> tuple[int, int]:
    for i in range(1,len(numbers)):
        if numbers[i] + numbers[i-1] >= target:
            return i-1, i



import typeguard

@typeguard.typechecked
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = find_start_pointers(numbers, target)
        condition = True
        while condition:
            if left < 0 or right >= len(numbers):
                condition = False
                error = "No solution found"
                raise ValueError(error)
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                left -= 1
            else:
                right += 1


task = Solution()
print(task.twoSum([2,7,11,15], 9)) # [1,2]
print(task.twoSum([2,3,4], 6)) # [1,3]