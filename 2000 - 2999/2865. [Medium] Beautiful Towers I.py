# https://leetcode.com/problems/beautiful-towers-i/

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def helper(i):
            ans = 0 
            
            minValue = maxHeights[i]
            
            for j in range(i, -1 ,-1):
                minValue = min(minValue,maxHeights[j])
                
                ans += minValue
            
            minValue = maxHeights[i]
            
            for j in range(i + 1, n):
                minValue = min(minValue, maxHeights[j])
                
                ans += minValue
            
            return ans 
            
        n = len(maxHeights)
        
        ans = 0 
        
        for i in range(n):
            ans = max(ans, helper(i))
            
        return ans 
