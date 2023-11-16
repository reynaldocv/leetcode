# https://leetcode.com/problems/distribute-candies-among-children-i/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        @cache
        def helper(children, candies):
            if children == 0:
                if candies == 0: 
                    return 1 
                
                else: 
                    return 0 
                
            else: 
                ans = 0 
                for candie in range(limit + 1):
                    ans += helper(children - 1, candies - candie)
                    
                return ans 
            
        return helper(3, n)
