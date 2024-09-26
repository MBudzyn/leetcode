# IDEA
# We can solve this problem by using hash table, and iterate two times through the list.
# First time, we will create a copy of the list, but without random pointers, and at the
# same time we will create a hash table that will store the values and the pointers to the nodes
# of the copied list. Second time, we will iterate through the list and we will assign the random
# pointers to the copied list by using the hash table.
# TIME COMPLEXITY
# O(N) because we iterate two times through the list
# SPACE COMPLEXITY
# O(N) because we create a hash table that will store the values and the pointers to the nodes
# of the copied list. Also, we create a copy of the list.

