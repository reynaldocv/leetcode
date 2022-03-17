# https://leetcode.com/problems/stone-game-vii/

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @cache
        def helper(i, j):
            if i >= j:
                return 0
            else:
                val1 = min(stones[i + 1] + helper(i + 2, j), stones[j] + helper(i + 1, j - 1))
                val2 = min(stones[j - 1] + helper(i, j - 2), stones[i] + helper(i + 1, j - 1))
                
                return max(val1, val2)
            
        return helper(0, len(stones) - 1)
      
class Solution2:
    def stoneGameVII(self, stones: List[int]) -> int:
        @cache
        def helper(start, end):
            if start == end: 
                return 0 
            else: 
                ans = 0 
                ans = max(ans, prefix[end] - prefix[start + 1] - helper(start + 1, end))
                ans = max(ans, prefix[end - 1] - prefix[start] - helper(start, end - 1))
                
                return ans 
        
        prefix = [0]
        
        for stone in stones: 
            prefix.append(prefix[-1] + stone)
        
        return helper(0, len(stones))
