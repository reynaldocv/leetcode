# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(value):
            ans = 0 
            
            for candie in candies: 
                ans += candie//value
                
            return ans >= k 
            
        aSum = sum(candies)
        
        if aSum < k: 
            return 0 
        
        start = 0
        end = aSum + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                start = middle 
                
            else: 
                end = middle 
                
        return start
        
