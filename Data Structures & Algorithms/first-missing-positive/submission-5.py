class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums.sort()

        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
        
        if i == len(nums) or nums[i] != 1:
            return 1

        j = i + 1

        while j < len(nums):
            diff = nums[j] - nums[i]

            if diff == 0:
                j += 1
            elif diff == 1:
                i = j
                j += 1
            else:
                return nums[i] + 1
        
        return nums[i] + 1





        


            



        





                
            
        


                

