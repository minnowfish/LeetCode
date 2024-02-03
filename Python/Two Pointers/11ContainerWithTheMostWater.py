class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = (r-l) * min(height[l],height[r])
        h = max(height)
        
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            maxArea = max((r-l) * min(height[l],height[r]), maxArea)
            if (r-l)*h <= maxArea:
                break
        return(maxArea)
