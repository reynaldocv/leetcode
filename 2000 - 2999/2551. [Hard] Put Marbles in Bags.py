# https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        pairs = [0 for _ in range(n - 1)]
        
        for i in range(n - 1):
            pairs[i] = weights[i] + weights[i + 1]
            
        pairs.sort()
        
        ans = 0
        
        for i in range(k - 1):
            ans += pairs[n - 2 - i] - pairs[i]
            
        return ans

