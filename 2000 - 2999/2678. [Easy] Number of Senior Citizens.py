# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0 
        
        for string in details: 
            age = int(string[11: 13])
            
            if age > 60: 
                ans += 1 
                
        return ans 
                
        
