# https://leetcode.com/problems/allocate-mailboxes/

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        @cache
        def helper(n, k):
            if n <= k: 
                return 0
            
            if k == 1: 
                return mdist[0][n - 1]
            
            ans = inf  
            for i in range(k - 1, n): 
                ans = min(ans, helper(i, k - 1) + mdist[i][n - 1])
            return ans 
        
        houses.sort()
        n = len(houses)
        
        mdist = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n): 
                mdist[i][j] = mdist[i][j - 1] + houses[j] - houses[i + j >> 1]
        
        return helper(n, k)
        
