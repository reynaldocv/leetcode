# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        limit = max(max([x for (x, _) in fruits]), startPos) + k
        
        n = len(fruits)
        prefix = [0 for _ in range(limit + 1)]
        
        for (x, fruit) in fruits: 
            prefix[x] = fruit
        
        for i in range(1, limit + 1):
            prefix[i] += prefix[i - 1]
        
        ans = 0 
        for i in range(max(0, startPos - k), startPos + k + 1):
            if i <= startPos: 
                res = k - (startPos - i)
                right = max(i + res, startPos)                
                left = prefix[i - 1] if i >= 1 else 0 
                ans = max(ans, prefix[right] - left)
            else: 
                res = k - (i - startPos)
                idx = min(i - res, startPos)                
                left = prefix[idx - 1] if idx >= 1 else 0                
                ans = max(ans, prefix[i] - left)
            
        return ans
            
        
