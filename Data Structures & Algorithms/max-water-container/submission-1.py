class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = (j-i)*min(heights[i], heights[j])
                areas.append(area)
        
        return max(areas)
        