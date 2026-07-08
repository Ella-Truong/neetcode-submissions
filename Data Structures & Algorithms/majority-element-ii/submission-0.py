class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        output=[]
        for key, val in count.items():
            if val > math.floor(n/3):
                output.append(key)

        return output