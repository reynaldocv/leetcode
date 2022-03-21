# https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        def helper(a, b, c):
            if a + 1 == b and b + 1 == c: 
                return 0 
            elif b - a == 2 or c - b == 2 or a  + 1 == b or b + 1 == c:
                return 1
            else: 
                return 2
            
        minElem = min([a, b, c])
        maxElem = max([a, b, c])
        midElem = a + b + c - minElem - maxElem 
        
        return [helper(minElem, midElem, maxElem), maxElem - minElem - 2]

        
            
