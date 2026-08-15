class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        product = 1
        for num in nums:
            prefix.append(product)
            product *= num

        suffix = []
        product = 1
        for num in reversed(nums):
            suffix.append(product)
            product *= num
        suffix.reverse()

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output