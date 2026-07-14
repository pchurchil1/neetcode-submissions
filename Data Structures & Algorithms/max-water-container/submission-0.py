class Solution:
    # Amount of water = min(left wall, right wall) * (right - left)
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        mostWater = 0
        while left < right:
            
            water = min(heights[left], heights[right]) * (right - left)
            mostWater = max(water, mostWater)

            if (heights[left] > heights[right]):
                right -=1
            else:
                left +=1


        return mostWater
        