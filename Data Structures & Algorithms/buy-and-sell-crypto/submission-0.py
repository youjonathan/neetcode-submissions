class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_i = 0
        mini = prices[min_i]

        while min_i < len(prices) - 1 and prices[min_i + 1] < mini:
            min_i += 1
            mini = prices[min_i]

        if min_i == len(prices) - 1:
            return 0

        max_i = min_i + 1
        maxi = prices[max_i]

        while max_i < len(prices) - 1:
            max_i += 1
            maxi = max(maxi, prices[max_i])

        if maxi < mini:
            return 0
        
        return maxi - mini