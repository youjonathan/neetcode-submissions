class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        print(nums)

        i = 0
        j = 1
        k = len(nums) - 1

        out = []
        
        while i < j and j < k:
            left_sum = nums[i] + nums[j]
            total = left_sum + nums[k]
            while total > 0 and j < k:
                k -= 1
                total = left_sum + nums[k]
            while total < 0 and i < j:
                i += 1
                total = left_sum + nums[k]
            if total == 0:
                out.append([nums[i], nums[j], nums[k]])
            j += 1

        return out