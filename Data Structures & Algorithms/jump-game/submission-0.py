class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        target = len(nums) - 1
        i = target - 1
        while i >= 0:
            need = target - i
            if nums[i] >= need:
                target = i
                i = target - 1
            else:
                i -= 1
        
        return target == 0