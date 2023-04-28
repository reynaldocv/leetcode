# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = {-1: 0}
        
        cnt = 0 
        
        ans = inf
        
        for (i, char) in enumerate(blocks):
            if char == "W":
                cnt += 1 
                
            if i >= k - 1: 
                ans = min(ans, cnt - counter[i - k])
                
            counter[i] = cnt
            
        return ans 

        
