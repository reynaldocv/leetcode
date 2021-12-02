# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []        
        envelopes.sort(key=lambda item: (item[0], -item[1]))        
        
        for envelope in envelopes: 
            idx = bisect_left(dp, envelope[1])
            if idx == len(dp):
                dp.append(envelope[1])
            else: 
                dp[idx] = envelope[1]
                
        return len(dp)
       
        
        
