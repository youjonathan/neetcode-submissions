class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        for num in nums[:len(nums) - 1]:
            new_rob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = new_rob
        
        rob3, rob4 = 0, 0
        for num in nums[1:]:
            new_rob = max(rob3 + num, rob4)
            rob3 = rob4
            rob4 = new_rob

        return max(rob2, rob4)