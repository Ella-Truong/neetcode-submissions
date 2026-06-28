class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            count, curr = 0, num
            while curr in numSet:
                count += 1
                curr += 1

            res = max(res, count)
            
        return res

        





