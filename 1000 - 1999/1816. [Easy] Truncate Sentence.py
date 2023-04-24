# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        counter = 0 
        
        ans = ""
        
        for char in s:
            if char == " ":
                counter += 1 
                
            if counter == k: 
                return ans
            
            ans += char 
            
        return ans 
        
