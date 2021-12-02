# https://leetcode.com/problems/can-i-win/

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def helper(mask, total):
            if total <= 0: 
                return False 
            
            for i in range(maxChoosableInteger): 
                if (mask >> i) & 1 == 0:
                    if helper(mask ^ (1 << i), total - (i + 1)) == False: 
                        return True 
            
            return False 
    
        if desiredTotal == 0: 
            return True 
        
        if maxChoosableInteger * (maxChoosableInteger+1)//2 < desiredTotal: 
            return False
        
        return helper(0, desiredTotal)
    
