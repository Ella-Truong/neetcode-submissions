class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_key = max(count, key=count.get)
        return max_key