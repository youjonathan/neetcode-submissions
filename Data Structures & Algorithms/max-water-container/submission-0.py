class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        area = 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = max(area, width * height)

            if heights[l + 1] > heights[l]:
                l += 1
            elif heights[r - 1] > heights[r]:
                r -= 1
            else:
                break
        
        return area