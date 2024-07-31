# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution:
    def maxOperations(self, s: str) -> int:
        cnt = 0 
        space = False
        
        ans = 0
        
        for char in s + "1": 
            if char == "1":
                if space == True: 
                    ans += cnt 
                    
                    space = False 
                    
                cnt += 1 
                
            else: 
                space = True 
                
        return ans 
