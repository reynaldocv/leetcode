# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        left = [num + i for (i, num) in enumerate(values)]
        right = [num - i for (i, num) in enumerate(values)]
        
        for i in range(1, n):
            left[i] = max(left[i - 1], left[i])
            
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], right[i])
            
        ans = -inf
        
        for i in range(n - 1):
            ans = max(ans, left[i] + right[i + 1])
            
        return ans 
        
