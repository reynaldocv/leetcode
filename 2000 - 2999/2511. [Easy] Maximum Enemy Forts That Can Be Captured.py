# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        prev = 0 
        
        ans = 0 
        
        counter = 0 
        
        for num in forts: 
            if num == 0: 
                counter += 1 
            
            else: 
                if (num == -prev): 
                    ans = max(ans, counter)
                    
                counter = 0 
                prev = num 
                    
        return ans 
            
