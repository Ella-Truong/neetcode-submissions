class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        uniqueList = []
        for key, val in count.items():
            if val == 1:
                uniqueList.append(key)
        
        if not uniqueList:
            return -1

        return max(uniqueList)
