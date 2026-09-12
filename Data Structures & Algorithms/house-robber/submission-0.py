class Solution:
    def rob(self, nums: List[int]) -> int:
        
        total = 0
        even = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even += num
            total += num
        
        return even if total - even < even else total - even