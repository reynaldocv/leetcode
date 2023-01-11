# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) 
        
        seen = set([])
        
        for candy in candyType: 
            seen.add(candy)
                        
        return min(n//2, len(seen))
        
