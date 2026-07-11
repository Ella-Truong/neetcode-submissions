class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        globalMin = arrays[0][0]
        globalMax = arrays[0][-1]

        maxDist = 0
        for i in range(1, len(arrays)):
            currMin = arrays[i][0]
            currMax = arrays[i][-1]

            maxDist = max(
                maxDist,
                abs(globalMax - currMin),
                abs(currMax - globalMin)
            )

            globalMin = min(globalMin, currMin)
            globalMax = max(globalMax, currMax)

        return maxDist
            

        