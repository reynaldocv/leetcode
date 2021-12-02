# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)        
        right = [values[i] - i for i in range(n)]
        
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1])
        
        ans = 0
        for i in range(n - 1):
            left = i + values[i]
            ans = max(ans, left + right[i + 1])
                      
        return ans
        
