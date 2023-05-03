# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        def helper(array):
            for i in range(1, n):
                array[i] = max(array[i], array[i- 1])
                
            return array
        
        n = len(values)
        
        left = [num + i for (i, num) in enumerate(values)]
        right = [num - i for (i, num) in enumerate(values)]
        
        left = helper(left)
        right = helper(right[:: -1])[:: -1]
        
        ans = -inf
        
        for i in range(n - 1):
            ans = max(ans, left[i] + right[i + 1])
            
        return ans 
        
        
