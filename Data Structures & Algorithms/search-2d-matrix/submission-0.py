class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # okay so brute force would just turn the matrix into a List
        # and then run binary search over int

        nums = [item for row in matrix for item in row]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return True

        return False