# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        prev = "$"
        cnt = 0        
        
        ans = ""
        
        for char in word + "$":
            if char != prev: 
                if cnt != 0: 
                    ans += str(cnt) + prev
                    
                cnt = 1 
                    
            else: 
                if cnt == 9: 
                    ans += str(9) + char 
                    
                    cnt = 0
                    
                cnt += 1 
                
            prev = char 
            
        return ans 
