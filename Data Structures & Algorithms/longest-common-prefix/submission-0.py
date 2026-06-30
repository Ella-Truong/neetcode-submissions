class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortest = min(strs, key=len)
        
        res = []
        i = 0
        for i in range(len(sortest)):
            if all(s[i] == sortest[i] for s in strs):
                res.append(sortest[i])
            else:
                break
        
        return "".join(res)



            
