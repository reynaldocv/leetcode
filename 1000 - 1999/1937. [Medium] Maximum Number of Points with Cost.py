# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def helper(arr):
            ans = [num for num in arr]
            
            for i in range(1, n):
                ans[i] = max(arr[i], ans[i - 1] - 1)
                
            return ans 
        
        m, n = len(points), len(points[0])
        
        ans = [0 for _ in range(n)]
        
        for row in points: 
            left = helper(ans)
            right = helper(ans[:: -1])[:: -1]
            
            for i in range(n):
                ans[i] = row[i] + max(left[i], right[i])
            
        return max(ans)
                
