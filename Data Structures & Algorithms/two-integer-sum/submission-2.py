class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexednums = []
        for i in range(len(nums)):
            indexednums.append([nums[i], i])
        
        A = sorted(indexednums)
        
        i, j = 0, len(nums) - 1
        while (i < j):
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
            
