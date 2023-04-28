# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        
        ans = ""
        
        for i in range(n - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                ans = max(ans, num[i]*3)
                
        return ans 
            
        
