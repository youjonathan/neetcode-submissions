class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        memo = {}

        def findCombinations(i, curr_amount):
            if (i, curr_amount) in memo:
                return memo[(i, curr_amount)]
            if i >= len(coins) or curr_amount > amount:
                return math.inf
            if curr_amount == amount:
                return 0
            memo[(i, curr_amount)] = min(1 + findCombinations(i, curr_amount + coins[i]), findCombinations(i + 1, curr_amount))
            return memo[(i, curr_amount)]

        lowest = findCombinations(0, 0)
        return -1 if lowest == math.inf else int(lowest)