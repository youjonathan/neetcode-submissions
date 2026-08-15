class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        non_zero = 1
        for num in nums:
            product *= num
            if num != 0:
                non_zero *= num

        output = []
        for num in nums:
            if num == 0:
                output.append(int(non_zero))
            else:
                output.append(int(product / num))

        return output