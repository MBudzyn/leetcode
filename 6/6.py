# IDEA
# to solve this problem, we can create 2D array that on each lvl will store
# the letters of the layer of the zigzag pattern of the string
# then we will iterate through the word and by changing direction we will by
# adding the letters to the array on the correct level
# then we will iterate through the array and concatenate the letters
# TIME COMPLEXITY
# O(N) because we iterate through the word
# SPACE COMPLEXITY
# O(N) because we store the letters in the 2D array

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[""] for _ in range(numRows)]
        dir = 1
        target = 0

        for i in range(len(s)):
            res[target].append(s[i])
            target += dir
            if target == numRows:
                dir = -1
                target = numRows - 2
            elif target == -1:
                dir = 1
                target = 1
        return "".join(["".join(x) for x in res])
