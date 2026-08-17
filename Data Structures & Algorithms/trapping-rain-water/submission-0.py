class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = 0
        right_max = 0

        l = 0
        r = len(height) - 1

        total = 0

        while l < r:
            left_curr = height[l]
            right_curr = height[r]

            left_max = max(left_max, left_curr)
            right_max = max(right_max, right_curr)

            if left_curr < right_curr:
                total += left_max - left_curr
                l += 1
            else:
                total += right_max - right_curr
                r -= 1
        
        return total