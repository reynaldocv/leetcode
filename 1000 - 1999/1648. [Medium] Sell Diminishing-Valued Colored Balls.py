# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def helper(x):
            ans = 0 
            for total in inventory: 
                ans += max(0, total - x)
                
            return ans
            
        MOD = 10**9 + 7
         
        start = 0 
        end = 10**9
        
        while end - start > 0 : 
            m = (end + start + 1)//2
            if helper(m) < orders: 
                end = m - 1
            else: 
                start = m    
                
        ans = 0 
        
        for total in inventory: 
            if total > start: 
                ans += (total + start + 1)*(total - start)//2
                
        return (ans - (helper(start) - orders) * (start + 1)) % MOD
                
