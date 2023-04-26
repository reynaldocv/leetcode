# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = 0 
        
        num = ""
        
        for char in s + "$":
            if char in "0987654321":
                num += char 
            
            else: 
                if num:
                    if last >= int(num):
                        return False 
                    
                    last = int(num)
                
                num = ""
                
        return True
                    
                    
        
        
        
