class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        # print(nums)

        i = 0
        l = 1
        r = len(nums) - 1

        out = []
        
        while i < len(nums) - 2:
            target = -nums[i]
            summed = nums[l] + nums[r]
            
            while summed != target and l < r:
                if summed > target:
                    r -= 1
                else:
                    l += 1
                summed = nums[l] + nums[r]

            if summed == target and l < r:
                out.append([nums[i], nums[l], nums[r]])

            i += 1
            l = i + 1
            r = len(nums) - 1

        return out