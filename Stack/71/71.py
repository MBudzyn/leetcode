# IDEA
# we can solve this problem by implementing stack as array
# first put the all non-Null elements to the stack
# then delete all single "." symbols and iterate through the stack
# by deleting the last element if the element is equal to ".."
# TIME COMPLEXITY
# O(N) because we iterate through the string
# SPACE COMPLEXITY
# O(N) because we use stack to store the elements

class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split("/")
        tmp = [x for x in tmp if x]
        tmp = [x for x in tmp if x != "."]
        res = []
        for i in tmp:
            if i == "..":
                if res:
                    res.pop()
            else:
                res.append(i)
        return "/" + "/".join(res)
