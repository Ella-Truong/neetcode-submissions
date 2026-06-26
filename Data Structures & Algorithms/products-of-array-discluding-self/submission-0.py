class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            nums_to_prod = nums[0:i] + nums[i+1:]
            prod = math.prod(nums_to_prod)
            result.append(prod)
        
        return result