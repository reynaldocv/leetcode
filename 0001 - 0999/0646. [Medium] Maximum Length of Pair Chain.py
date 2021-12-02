# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1 for _ in range(n)]
        
        pairs.sort()
        
        ans = 1
        
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]: 
                    dp[i] = max(dp[i], dp[j] + 1)
                    
            ans = max(ans, dp[i])
            
        return ans
      
class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:                
        pairs.sort(key = lambda item: item[1])
        
        cur = -inf        
        ans = 0
        
        for (x, y) in pairs:
            if cur < x:
                cur = y
                ans += 1
        
        return ans
            
            
               
            
            
            
            
                
            
