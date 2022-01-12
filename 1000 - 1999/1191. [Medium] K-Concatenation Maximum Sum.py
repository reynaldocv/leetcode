# https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        ans = -inf
        prev = 0
        for num in arr:
            prev += num            
            if prev < 0: 
                prev = 0
            
            ans = max(ans, prev)
        
        if k == 1:
            return ans
        
        aSum = sum(arr)                
        sumLeft, sumRight = 0, 0        
        left, right = 0, 0
        
        for i in range(n): 
            right += arr[i]
            sumRight = max(sumRight, right)
            left += arr[n - 1 - i]
            sumLeft = max(sumLeft, left)
        
        if aSum <= 0:
            ans = max(ans, sumLeft + sumRight)
        else: 
            ans = max(ans, sumLeft + aSum*(k - 2) + sumRight)
        
        return ans % MOD
