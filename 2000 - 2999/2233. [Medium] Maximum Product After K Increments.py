# https://leetcode.com/problems/maximum-product-after-k-increments/

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        heap = []
        
        for num in nums: 
            heappush(heap, num % MOD)
            
        for _ in range(k):
            num = heappop(heap)
            
            heappush(heap, (num + 1) % MOD) 
            
        ans = 1 
        
        while heap: 
            ans = (ans*heappop(heap)) % MOD
            
        return ans 
        
        

                
        
