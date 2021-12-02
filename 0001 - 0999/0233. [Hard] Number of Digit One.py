# https://leetcode.com/problems/number-of-digit-one/

class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0 
        
        strN = str(n)
        n = len(strN)
        
        for (i, val) in enumerate(strN):
            left = int(strN[:i]) if i > 0 else 0
            right = int(strN[i + 1:]) if i < n - 1 else 0
            if val == "0": 
                if i == n - 1:
                    ans += left
                else: 
                    ans += (left)*10**(n - i - 1)              
            elif val == "1":
                if i == n - 1:
                    ans += (left + 1)
                else:                                 
                    ans += (left)*10**(n - i - 1) + (right + 1)
            else:
                if i == 0: 
                    ans += 10**(n - i - 1)
                else:
                    ans += (left + 1)*10**(n - i - 1)
                
        return ans
                
            
                
                
                
        
