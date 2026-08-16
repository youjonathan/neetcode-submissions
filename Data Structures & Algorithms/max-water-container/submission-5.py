class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = max(area, width * height)

            if heights[r] >= heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return area