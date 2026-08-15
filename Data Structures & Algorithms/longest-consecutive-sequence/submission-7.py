class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        # print("set_nums: " + str(set_nums))
        longest = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                # print(num)
                long = 0
                for i in range(len(set_nums)):
                    if num + i in set_nums:
                        long += 1
                    else:
                        break
                # print(long)
                longest = max(long, longest)

        return longest