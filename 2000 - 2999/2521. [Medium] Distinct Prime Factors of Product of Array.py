# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        limit = max(nums) + 1
        
        factors = [[] for i in range(limit)]
        
        for i in range(2, limit):
            if not factors[i]:
                for j in range(i, limit, i):
                    factors[j].append(i)
                    
        ans = set() 
        
        for num in nums: 
            for factor in factors[num]:
                ans.add(factor)
                
        return len(ans)
        
