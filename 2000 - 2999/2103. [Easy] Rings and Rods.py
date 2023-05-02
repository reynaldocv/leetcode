# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) 
        
        counter = defaultdict(lambda: [0, 0, 0])
        
        index = {"G": 0, "R": 1, "B": 2}
        
        for i in range(n//2):
            color = rings[2*i]
            position = rings[2*i + 1]
            
            idx = index[color]
            
            counter[position][idx] = 1 
            
        ans = 0    
        
        for key in counter:
            if sum(counter[key]) == 3: 
                ans += 1 
                
        return ans 
            
            
        
        
