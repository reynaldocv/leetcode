# https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        def helper(value):
            tmp = volume + n*value
            
            biggest = diff + value
            
            unpair = max(tmp % 2, 2*biggest - tmp)
            
            pair = (tmp - unpair)//2
            
            return unpair*cost1 + pair*cost2
        
        MOD = 10**9 + 7
            
        n = len(nums)
        
        maxElem = max(nums)
        minElem = min(nums)

        volume = maxElem*n - sum(nums)

        diff = maxElem - minElem 
        
        if 2*cost1 <= cost2 or n <= 2: 
            return (volume*cost1) % MOD
        
        more = max(0, diff * 2 - volume)//(n - 2) 
            
        ans = volume*cost1 
        
        for extra in [0, 1, more, more + 1, more + 2]:
            ans = min(ans, helper(extra))                
                       
        return ans % MOD 
    
