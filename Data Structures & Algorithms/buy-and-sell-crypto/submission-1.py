class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]

        max_diff = 0

        for num in prices:
            minimum = min(minimum, num)
            max_diff = max(max_diff, num - minimum)

        return max_diff if max_diff > 0 else 0