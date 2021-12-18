# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        strN = str(n)
        k = len(strN)
        
        dp = [0 for _ in range(k)] + [1]
        
        for i in range(k - 1, -1, -1):
            for digit in digits: 
                if digit < strN[i]:
                    dp[i] += m**(k - i - 1)
                
                elif digit == strN[i]:
                    dp[i] += dp[i + 1]
                    
        ans = 0 
        for i in range(1, k):
            ans += m**i
            
        return ans + dp[0]
                
        
        
