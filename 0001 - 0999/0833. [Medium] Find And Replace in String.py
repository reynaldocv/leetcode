# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        seen = {index: i for (i, index) in enumerate(indices)}
        ans = ""
        
        start, n = 0, len(s)
                
        while start < n:
            go = False 
            if start in seen: 
                source = sources[seen[start]]
                target = targets[seen[start]]
                j = 0
                while j < len(source) and s[start + j] == source[j]:
                    j += 1 
                    
                if j == len(source):
                    start += j 
                    ans += target
                    go = True
        
            if go == False: 
                ans += s[start]
                start += 1 

        return ans 
                
                
                
