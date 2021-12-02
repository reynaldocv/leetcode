# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        strN = "0"        
        for num in range(1, n + 1):
            strN += str(bin(num))[2:]
        
        return int(strN, 2) % (10**9 + 7)
       
class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        modExp = MOD - 1
        
        length = 0
        ans = 0
        
        for num in range(1, n + 1):
            if num & num - 1 == 0:
                length += 1
                
            ans = (ans*2**(length % modExp) + num) % MOD
            
        return ans       

        
