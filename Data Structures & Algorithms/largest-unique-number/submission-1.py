class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = -1

        for num, freq in count.items():
            if freq == 1:
                ans = max(ans, num)

        return ans
