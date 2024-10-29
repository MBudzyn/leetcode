# IDEA at the beginning, we will make the biggest size of the substring without repeating characters then we will be
# moving this size window to the right if the substring is not valid anymore (repeating characters) or we will be
# moving right pointer to the right if the substring is valid (no repeating characters) TIME COMPLEXITY most hard to
# understand is the time complexity of this algorithm is moment when we are checking if the new substring is valid
# because we are moving window to the right by one element, we only need to check if the new element is in the
# substring and if it is, we need to move the left and right pointer to the right until we will not have repeating
# characters in the substring. to check if the element is in the substring we can use the hash table, so the time
# complexity of this operation is O(1) and because we are iterating the string only once, the time complexity of this
# algorithm is O(n) SPACE COMPLEXITY the space complexity is O(n) because we are using the hash table to store the
# characters from the string with their indexes

import typeguard
@ typeguard.typechecked
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length



s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
print(s.lengthOfLongestSubstring("bbbbb"))  # 1
