# https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:
        def helper(s):
            Ones, Zeros = [], []
            cnt0, cnt1 = 0, 0
            
            for char in s: 
                if char == "0":
                    cnt0 += 1 
                    
                if char == "1":
                    cnt1 += 1 
                    
                Zeros.append(cnt0)
                Ones.append(cnt1)
                
            return Zeros, Ones
        
        n = len(s) 
        
        leftZeros, leftOnes = helper(s)
        rightZeros, rightOnes = helper(s[:: -1])
        
        rightZeros = rightZeros[:: -1]
        rightOnes = rightOnes[:: -1]
        
        ans = 0 
        
        for i in range(1, n - 1):
            if s[i] == "0": 
                ans += leftOnes[i - 1]*rightOnes[i + 1]
                
            else: 
                ans += leftZeros[i - 1]*rightZeros[i + 1]
                
        return ans 
        
