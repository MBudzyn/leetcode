# IDEA
# we can handle only one stock at a time, but we can sell it the same day we buy it
# we want to sell stock always when we can make a profit and actualize stock we handle
# buy one we are buying or actualizing stock we handle with the lowest price we can
# TIME COMPLEXITY
# the time complexity is O(n) because we only need to iterate the array once
# SPACE COMPLEXITY
# the space complexity is O(1)

import typeguard
@ typeguard.typechecked

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sum = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > min:
                sum += prices[i] - min
            min = prices[i]

        return sum


