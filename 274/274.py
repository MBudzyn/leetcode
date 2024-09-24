# IDEA
# becouse of the definition of h-index first idea that comes to mind is to sort the array and then iterate through it
# and check if the current element is greater than the number of elements that are greater than it
# if so we can actualize the cd result and return it at the end but if it is not the case we can actualize the result
# with the maximum value of the current result and the current element
# TIME COMPLEXITY
# The time complexity is O(nlogn) because we need to sort the array
# SPACE COMPLEXITY
# The space complexity is O(1) because we only need to use constant number of variables

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        max_h = 0
        for i in range(len(citations)):
            cd = 0
            if len(citations) - i >= citations[i]:
                cd = citations[i]
            elif citations[i] > len(citations) - i:
                cd = len(citations) - i

            max_h = max(max_h, cd)
        return max_h