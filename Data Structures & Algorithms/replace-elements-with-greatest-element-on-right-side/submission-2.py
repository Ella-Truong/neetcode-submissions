class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        n = len(arr)
        res = [0]*n
        
        for i in range(n-1, -1, -1):
            res[i] = max_right
            max_right = max(arr[i], max_right)
        
        return res

