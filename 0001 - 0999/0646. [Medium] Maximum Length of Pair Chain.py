# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda item: item[1])
        
        last = -inf
        ans = 0 
        
        for (start, end) in pairs: 
            if last < start: 
                ans += 1 
                
                last = end 
        
        return ans 
            
            
               
            
            
            
            
                
            
