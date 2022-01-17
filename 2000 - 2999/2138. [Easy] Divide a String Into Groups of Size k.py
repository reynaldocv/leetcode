# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(0, n , k):
            ans.append(s[i: i + k])
        
        if ans:
            ans[-1] += fill*(k - len(ans[-1]))
            
        return ans
                             
                             
                       
    
