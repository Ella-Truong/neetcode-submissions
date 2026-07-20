class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        for i in range(n):
            maxLeft = 0
            for j in range(i+1):
                maxLeft = max(maxLeft, height[j])

            maxRight = 0
            for j in range(i, n):
                maxRight = max(maxRight, height[j])
            
            water += min(maxLeft, maxRight) - height[i]

        return water