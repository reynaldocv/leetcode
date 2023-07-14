# https://leetcode.com/problems/minimum-suffix-flips/

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        
        start = 0 
        
        while start < n and target[start] == "0":
            start += 1 
            
        if start == n: 
            return 0 
        
        ans = 1 
        
        for i in range(start + 1, n):
            if target[i] != target[i - 1]:
                ans += 1 
                
        return ans 
            
