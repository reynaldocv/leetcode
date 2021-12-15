# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        prev = 0 
        for i in range(n):
            left[i] = prev + 1 if s[i] == "1" else prev
            prev = left[i]
            
        prev = 0 
        for i in range(n - 1, -1, -1):
            right[i] = prev + 1 if s[i] == "0" else prev
            prev = right[i]
        
        ans = inf
        
        for i in range(n + 1):
            prefix = left[i - 1] if i - 1 >= 0 else 0 
            suffix = right[i] if i < n else 0 
            
            ans = min(ans, prefix + suffix)
    
        return ans
            
class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zeros = 0
        
        for char in s: 
            if char == "0":
                zeros += 1
                
        ans = zeros 
        ones = 0 
        for char in s:
            if char == "1":
                ones += 1
            else: 
                zeros -= 1
            
            ans = min(ans, ones + zeros)
            
        return ans        
