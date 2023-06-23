# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0 
        
        ans = 0 
        
        for row in bank: 
            cnt = 0 
            
            for char in row: 
                if char == "1":
                    cnt += 1 
                    
            if cnt != 0: 
                ans += prev*cnt
                
                prev = cnt 
    
        return ans 
        
        
