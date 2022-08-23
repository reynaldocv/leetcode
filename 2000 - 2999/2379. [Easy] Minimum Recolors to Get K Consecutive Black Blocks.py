# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf 
        seen = defaultdict(lambda: 0)
        
        counter = 0 
        
        for (i, char) in enumerate(blocks):
            counter += 1 if char == "B" else 0             
            if i >= k:
                ans = min(ans, k - (counter - seen[i -  k]))            
            seen[i] = counter
            
        return ans 
