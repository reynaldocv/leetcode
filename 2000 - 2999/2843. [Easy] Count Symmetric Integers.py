# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def helper(strNum):
            n = len(strNum)
            
            if n % 2 == 1: 
                return False 
            
            left = right = 0 
            
            for i in range(n//2):
                left += int(strNum[i])
                right += int(strNum[n - 1 - i])
                
            return left == right
        
        ans = 0
        
        for i in range(low, high + 1):
            if helper(str(i)):
                ans += 1 
                
        return ans
                
            
            
