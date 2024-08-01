# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
            
        ans = 0 
        
        for key in counter: 
            if counter[key] % 2 == 1: 
                ans += 1 
                
            else: 
                ans += 2
            
        return ans 
        
        
        
