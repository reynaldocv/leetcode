# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def helper(value):
            counter = dp[value]
            
            quo = n//value
            
            for i in range(quo):
                counterEnd = dp[(i + 1)*value]
                counterStart = dp[i*value]
                
                cnt = ()
                
                for i in range(26):
                    diff = counterEnd[i] - counterStart[i]
                    
                    cnt += (diff, )
                    
                if counter != cnt: 
                    return False 
                
            return True 
        
        n = len(s)
        
        index = {chr(ord("a") + i): i for i in range(26)}
        
        dp = [(0, )*26]
        
        for char in s: 
            idx = index[char]
            
            counter = dp[-1]
            
            counter = counter[: idx] + (counter[idx] + 1, ) + counter[idx + 1: ]
            
            dp.append(counter)
            
        for i in range(1, n + 1):
            if n % i == 0: 
                if helper(i):
                    return i 
                
                

        
        
        
