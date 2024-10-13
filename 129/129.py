# IDEA
# we can solve this problem by using recursion
# if the node is the leaf, (node.left is None and node.right is None) then we return node.value
# otherwise, we actualize the value of the sons which are not None and return sum of the recursive call
# on the left and right sons
# TIME COMPLEXITY
# O(n) -- we visit every node once
# SPACE COMPLEXITY
# O(h) -- h is the height of the tree, the maximum depth of the recursion stack which in worst case is O(n)

