# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution:
    def beautySum(self, s: str) -> int:        
        n = len(s)
        ans = 0 
        
        for i in range(n):
            counter = defaultdict(lambda: 0)
            for char in s[i:]:                
                counter[char] += 1 
                hMax, hMin = 0, inf            
                for key in counter: 
                    hMax = max(hMax, counter[key])
                    hMin = min(hMin, counter[key])
                    
                ans += hMax - hMin
                
        return ans
            
        
