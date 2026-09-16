class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        def findCombinations(i, curr_amount):
            if i >= len(coins) or curr_amount > amount:
                return math.inf
            if curr_amount == amount:
                return 0
            return min(1 + findCombinations(i, curr_amount + coins[i]), findCombinations(i + 1, curr_amount))

        lowest = math.inf
        for i in range(len(coins)):
            lowest = min(findCombinations(i, 0), lowest)

        return -1 if lowest == math.inf else int(lowest)