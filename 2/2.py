# IDEA
# problem solution is very simple, we will create empty list and iterate through the input lists
# at the same time and append sum of the elements % 10 + carry to the result list and update carry
# then we will repeat the process until we reach the end of one of the one or both lists
# then we need to check if one lists is not empty and add the rest of the elements to the result list
# then we need to check if carry is greater than 0 and add it to the result list
# at the end we need to return the head of the result list
# TIME COMPLEXITY
# The time complexity is O(n) because we only need to iterate the lists once
# SPACE COMPLEXITY
# The space complexity is O(n) because we need to store the result list
