# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: 
            return 0 
        
        circle = n*2
        
        counter = defaultdict(lambda: 0)
        
        for i in range(n):
            counter[i*2] += 1 
            
        ans = 0 
            
        for key in counter:     
            if counter[key] > 0: 
                if key + n in counter: 
                    counter[key + n] -= 1 
                    
                counter[key] -= 1 
                
                ans += 1 
            
        return ans 
