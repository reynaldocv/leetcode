# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: 
            return [0]
        elif n == 1: 
            return [0, 1]
        else:
            ans = [0, 1]
            start = 0 
            limit = 2
            for _ in range(2, n + 1):
                if start >= limit: 
                    start = 0
                    limit *= 2 
                
                ans.append(ans[start] + 1)                    
                start += 1
            
            return ans 
        
