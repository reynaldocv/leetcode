# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        seen = defaultdict(lambda: {})
        
        n = len(rings)
        for i in range(n//2):
            color = rings[2*i]
            rod = int(rings[2*i + 1])
            seen[rod][color] = True
            
        ans = 0
        for i in range(10):
            if len(seen[i]) == 3: 
                ans += 1
                
        return ans
        
        
