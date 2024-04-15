# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def helper(value):
            ans = 0 
            
            for i in range(1, n + 1):
                for comb in combinations(coins, i):
                    mcm = 1 
                    
                    for num in comb: 
                        mcm = lcm(mcm, num)
                    
                    ans += (-1)**(i + 1)*(value//mcm)
                    
            return ans 
        
        n = len(coins)
        
        start = 0 
        end = k*min(coins) + 1
        
        while end - start > 1:  
            mid = (start + end)//2
            
            if helper(mid) < k: 
                start = mid
                
            else: 
                end = mid
                
        return end
