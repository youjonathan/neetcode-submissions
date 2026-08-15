class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        longest = 1
        for num in set_nums:
            if num - 1 in set_nums:
                longest += 1

        return longest