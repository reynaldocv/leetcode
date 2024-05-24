# https://leetcode.com/problems/smallest-good-base/

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def helper(value, exp):
            ans = 0 
            
            for i in range(exp + 1):
                ans += value**i
                
            return ans 
        
        n = int(n)
        
        totalBits = len(bin(n)[2: ])
        
        for exp in range(totalBits, 0, -1):
            start = 2 
            end = n - 1
            
            while end - start > 1: 
                mid = (end + start)//2
                
                if helper(mid, exp) < n: 
                    start = mid 
                    
                else: 
                    end = mid 
                    
            if helper(end, exp) == n: 
                return str(end)
                    
                    

