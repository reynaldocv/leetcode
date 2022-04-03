# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(value):
            ans = 0 
            for candie in candies: 
                ans += candie//value
                
                if ans >= k: 
                    return True
                    
            return False
            
        aSum = sum(candies)
        
        if aSum < k: 
            return 0 
        
        start = 1
        end = aSum + 1
        
        while end - start > 1: 
            mid = (end + start)//2
            if helper(mid): 
                start = mid
            else: 
                end = mid
                
        return start
