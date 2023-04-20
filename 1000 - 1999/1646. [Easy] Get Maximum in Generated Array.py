# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: 
            return n 
        
        arr = [0, 1] + [0 for _ in range(n - 1)]
        
        ans = 0 
        
        for i in range(2, n + 1):
            if i % 2 == 0: 
                arr[i] = arr[i//2]
                
            else:
                arr[i] = arr[i//2] + arr[i//2 + 1]
                
            ans = max(ans, arr[i])
                
        return ans
        
        
