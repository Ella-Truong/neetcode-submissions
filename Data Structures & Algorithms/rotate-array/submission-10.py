class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        if k == 0:
            return 
            
        half1 = nums[-k:]
        half2 = nums[:-k]
        nums[:k] = half1
        nums[k:] = half2
        
        