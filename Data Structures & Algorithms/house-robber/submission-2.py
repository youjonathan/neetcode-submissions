class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i: int):
            if i >= len(nums):
                return 0
            
            
            maximum = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return maximum
        
        return dfs(0)

