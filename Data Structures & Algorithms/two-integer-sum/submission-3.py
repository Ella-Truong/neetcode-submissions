class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            right = nums[i+1:]
            second = target-nums[i]
            if(second in right):
                return [i, i + 1 + right.index(second)]




        

            
