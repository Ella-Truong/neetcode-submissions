class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        j = 1
        while j < len(arr):
            arr[i] = max(arr[j:])
            i += 1
            j += 1
        arr[i] = -1
        return arr

