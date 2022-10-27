# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        side = 0 
        
        for (a, b) in rectangles: 
            side = max(side, min(a, b))
            
            counter[min(a, b)] += 1 
            
        return counter[side]
            
        
