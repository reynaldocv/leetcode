# https://leetcode.com/problems/can-convert-string-in-k-moves/

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n, m = len(s), len(t)
        
        if n != m: 
            return False
        
        counter = defaultdict(lambda: 0)
        for i in range(n):
            if s[i] != t[i]:
                diff = ord(t[i]) - ord(s[i])
                if diff > 0: 
                    counter[diff] += 1
                else: 
                    counter[26 + diff] += 1 
                    
        ans = 0 
        
        for key in counter: 
            ans = max(ans, (counter[key] - 1)*26 + key)
            
        return ans <= k 
                
       
        
