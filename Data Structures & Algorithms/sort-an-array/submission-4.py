import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            pivotIndex = random.randint(low, high)
            nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

            pivot = nums[high]
            i = low

            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]

            return i

        def quickSort(low, high):
            if low >= high:
                return
            
            pivotIndex = partition(low, high)

            quickSort(low, pivotIndex - 1)
            quickSort(pivotIndex + 1, high)

        quickSort(0, len(nums) - 1)

        return nums
    





