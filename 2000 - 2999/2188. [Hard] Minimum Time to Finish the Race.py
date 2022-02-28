# https://leetcode.com/problems/minimum-time-to-finish-the-race/

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        @cache 
        def helper(n):
            ans = arr[n - 1] if n <= 20 else inf 
            for m in range(1, min(20, n//2) + 1):
                ans = min(ans, helper(m) + helper(n - m) + changeTime)
        
            return ans 
        
        arr = [inf] * 20 
        for (f, r) in tires: 
            prefix = term = f
            for i in range(20):
                arr[i] = min(arr[i], prefix)
                term *= r 
                if term >= f + changeTime:
                    break
                
                prefix += term
        
        return helper(numLaps)
