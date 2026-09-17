class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # brute force method is loop over every subarray for a product
        # a more optimized way to do this is similar to palindromes
        # if we start at "centers" and move outward either to the left or the right
        # then we have guaranteed contiguous sequences?
        # idk if that actually even optimizes much though tbh
        # we can't just stop at negative numbers, because if there is an even number of negatives then we want them to be in the product

        # keep track of max and min
        # this is because min is going to be greatest num if negative and multiplied by another negative
        answer = -math.inf
        maximum = 1
        minimum = 1
        for x in nums:
            candidates = (x, maximum * x, minimum * x)
            maximum, minimum = max(candidates), min(candidates)
            answer = max(answer, maximum)
        
        return answer