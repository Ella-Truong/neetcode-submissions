class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        nums = set(nums)
        for num in nums.copy():
            if count[num] <= math.floor(n/3):
                nums.remove(num)

        return list(nums)
        