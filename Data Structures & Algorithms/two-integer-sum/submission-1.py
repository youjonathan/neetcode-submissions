class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in mydict:
                return [mydict[diff], index]
            mydict[num] = index