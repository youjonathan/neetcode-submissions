class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        past = {}

        # for each number, find the difference
        # then check if that alr exists in the hashmap
        for i, n in enumerate(nums):
            diff = target - n
            if diff in past:
                return [min(i, past[diff]), max(i, past[diff])]
            else:
                past[n] = i
        return []