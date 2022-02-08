# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        counter = {0: 1, 1: 0}
        
        prev = 0 
        ans = 0 
        
        for num in arr: 
            prev = (prev + num) % 2
            ans = (ans + counter[1 - prev]) % MOD
            counter[prev] += 1 
            
        return ans 
        
