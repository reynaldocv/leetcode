# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        
        limit = n//k 
        
        if n % k != 0: 
            limit += 1 
            
        ans = []
        
        for i in range(limit):
            ans.append(s[i*k: (i + 1)*k])
            
        while len(ans[-1]) < k: 
            ans[-1] += fill*(k - len(ans[-1]))
            
        return ans 
                    
                             
                       
    
