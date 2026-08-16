class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = 0
        m = 1
        r = 2

        out = []
        while r < len(nums) - 1:
            if nums[l] + nums[m] + nums[r] == 0:
                out.append([nums[l], nums[m], nums[r]])
            r += 1

            while m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    out.append([nums[l], nums[m], nums[r]])
                m += 1

                while l < m:
                    if nums[l] + nums[m] + nums[r] == 0:
                        out.append([nums[l], nums[m], nums[r]])
                    l += 1

        return out