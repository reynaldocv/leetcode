# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        prev = 0 
        
        ans = []
        
        for char in word: 
            prev = (prev*10 + int(char)) % m
            
            if prev == 0: 
                ans.append(1)
                
            else: 
                ans.append(0)
                
        return ans 
        
