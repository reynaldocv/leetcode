# https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for p, q in (1, 1), (1, -1), (-1, 1), (-1, -1): 
            val = low = inf 
            for (i, num1) in enumerate(arr1):
                num2 = arr2[i]
                
                ans = max(ans, num1*p + num2*q + i - low)
                low = min(low, num1*p + num2*q + i)
                
        return ans 
        
