class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        m = r // 2

        while l < r:
            if m == m + l:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m
                m = l + ((r - l) // 2)
            else:
                return nums[m]