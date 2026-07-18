class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        left = 0
        for i in range(len(heights)):
            for j in range(left + 1, len(heights)):
                area = (j-i)*min(heights[i], heights[j])
                areas.append(area)
        
        return max(areas)
        