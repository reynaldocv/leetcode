# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        prev = 0
        counter = defaultdict(lambda: 0)
        for char in s + "0": 
            if char == "1":
                prev += 1
            else:
                if prev != 0:                
                    counter[prev] += 1
                prev = 0
        
        ans = 0
        for key in counter: 
            ans += (key*(key + 1)//2)*counter[key]
            ans %= MOD
        
        return ans
                
                
            
            
        
