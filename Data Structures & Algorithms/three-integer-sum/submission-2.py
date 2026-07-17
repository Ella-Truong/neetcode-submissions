class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            fixed = nums[i]
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr = nums[left] + nums[right]
                
                if curr == -fixed:
                    res.append([fixed, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                elif curr < -fixed:
                    left += 1
                else: 
                    right -= 1
            
            i += 1

        return res
