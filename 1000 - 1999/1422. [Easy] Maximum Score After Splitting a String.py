# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0 
        ones = sum([1 for char in s if char == "1"])
        
        ans = 0 
        
        for char in s[: -1]:
            if char == "0":
                zeros += 1 
            else: 
                ones -= 1 
                
            ans = max(ans, zeros + ones)
            
        return ans 
            
        
