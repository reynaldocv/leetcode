# https://leetcode.com/problems/vowels-game-in-a-string/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0 
        
        for char in s: 
            if char in "aeiou":
                cnt += 1 
                
        if cnt % 2 == 1: 
            return True
        
        if cnt % 2 == 0 and cnt > 0: 
            return True 
        
        return False 
