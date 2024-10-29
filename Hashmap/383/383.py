# IDEA
# we will create a dict to store how many times each letter appears in the string
# then we will iterate through the second string and if the letter is in the dict we will decrement the value
# by 1 and if the value is less than 0 we will return False
# but if the letter is not in the dict we will return False
# at the end we will return True if we didn't return False before
# TIME COMPLEXITY
# The time complexity is O(n) because we need to iterate through the second string, and
# we are creating a dict with all the letters from the first string
# SPACE COMPLEXITY
# The space complexity is O(n) because in the worst case we will store all the letters from the first string
# with their counts

def construct_dict_ct(s: str) -> dict:
    dct = {}
    for c in s:
        if c in dct:
            dct[c] += 1
        else:
            dct[c] = 1
    return dct


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_r = construct_dict_ct(ransomNote)
        dict_m = construct_dict_ct(magazine)
        for key in dict_r.keys():
            if key not in dict_m or dict_r[key] > dict_m[key]:
                return False
        return True
