# IDEA
# we can solve this problem by iterating through the string and checking if
# the current character is equal to actual character we are looking for
# if it is, we can move the pointer to the right, if not, the pointer will stay in the same place
# at the end we can check if the pointer is out of the string and return True if it is
# in other case we can return False
# TIME COMPLEXITY
# O(n) because we iterate through the string
# SPACE COMPLEXITY
# O(1) because we only use constant number of variables

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0
        while s and ind < len(t):
            if s[0] == t[ind]:
                s = s[1:]
            ind += 1
        return not s

