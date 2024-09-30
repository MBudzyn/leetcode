# IDEA
# we can solve this problem by using greedy algorithm
# we iterate through the list from the second element to the end
# if the current element[0] is > then previous tmp, we add 1 to the result
# else we update the previous tmp[1] to the min(tmp, element[1])
# COMPLEXITY
# Time: O(n)
# Space: O(1)

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        srt = sorted(points)
        ct = 1
        limit = srt[0][1]
        for i in range(1, len(srt)):
            if srt[i][0] > limit:
                ct += 1
                limit = srt[i][1]
            else:
                limit = min(limit, srt[i][1])
        return ct
