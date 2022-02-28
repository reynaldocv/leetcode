# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0 
        
        cost = 0 
        start = 0 
        for (i, char) in enumerate(t):
            val = abs(ord(s[i]) - ord(t[i]))
            while start < i and cost + val > maxCost: 
                cost -= abs(ord(s[start]) - ord(t[start]))                
                start += 1  
            
            cost += val   
            if cost <= maxCost:
                ans = max(ans, i - start + 1)        
            
        return ans
