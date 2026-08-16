class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        sum = numbers[l] + numbers[r]
        while sum != target:
            if sum > target and l < r:
                r -= 1
            else:
                l += 1
            sum = numbers[l] + numbers[r]

        return [l + 1, r + 1]