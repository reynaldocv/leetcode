# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxElem = max(candies)
        
        ans = []
        
        for candie in candies: 
            ans.append(candie + extraCandies >= maxElem)
            
        return ans 
        
