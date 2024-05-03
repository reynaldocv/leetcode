# https://leetcode.com/problems/count-anagrams/

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        
        n = len(s)
        
        factorial = [1]
        divisor = [1]
        
        for i in range(1, n + 1):
            factorial.append(i % MOD) 
            divisor.append(pow(factorial[-1], -1, MOD))
            
        ans = 1 
        
        cnt = 0
        counter = defaultdict(lambda: 0)
        
        prev = 1
        
        for char in s + " ": 
            if char == " ":
                cnt = 0                 
                counter = defaultdict(lambda: 0)
                
                ans = (ans*prev) % MOD 
                
                prev = 1 
                
            else: 
                cnt += 1 
                counter[char] += 1 
                
                prev = (prev*factorial[cnt]*divisor[counter[char]]) % MOD 
                
        return ans 
                
                
        
                
                
        
