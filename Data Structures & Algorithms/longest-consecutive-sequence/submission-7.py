class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 0:
            return 0
        
        longest = curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
            
        return max(longest, curr)



        





