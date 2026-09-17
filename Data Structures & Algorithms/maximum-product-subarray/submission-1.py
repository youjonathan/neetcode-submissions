class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        answer = 0
        maximum = 1
        minimum = 1
        for num in nums:
            candidates = (num, maximum * num, minimum * num)
            maximum = max(candidates)
            minimum = min(candidates)
            answer = max(answer, maximum)
        
        return answer