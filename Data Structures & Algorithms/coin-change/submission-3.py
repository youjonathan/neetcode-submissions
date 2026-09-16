class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        memo = {}

        def findCombinations(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining < 0:
                return math.inf
            elif remaining == 0:
                return 0
            least = math.inf
            for coin in coins:
                least = min(1 + findCombinations(remaining - coin), least)
            memo[remaining] = least
            return memo[remaining]

        lowest = findCombinations(amount)
        return -1 if lowest == math.inf else int(lowest)