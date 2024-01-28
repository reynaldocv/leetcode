# https://leetcode.com/problems/utf-8-validation/

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def helper(number):
            if (number >> 7) == 0: 
                return 1 
            
            elif (number >> 5) == 6:
                return 2 
            
            elif (number >> 4) == 14:
                return 3 
            
            elif (number >> 3) == 30:
                return 4
            
            return 0
            
        cnt = 0 
        
        for num in data: 
            if cnt > 0: 
                if (num >> 6 != 2):
                    return False 
                
                else: 
                    cnt -= 1 
                    
            else: 
                cnt = helper(num) - 1
                
                if cnt < 0: 
                    return False 
                
        return cnt == 0  
