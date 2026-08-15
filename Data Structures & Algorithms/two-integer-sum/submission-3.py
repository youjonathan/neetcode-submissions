class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        indices = {}

        # store all numbers 
        for i, n in enumerate(nums):
            indices[n] = i

        # for each number, find the difference
        # then check if that exists in the hashmap
        # and then check if that has a different index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []