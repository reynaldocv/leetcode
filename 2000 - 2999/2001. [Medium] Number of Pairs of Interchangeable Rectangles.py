# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        ans = 0 
        
        for (a, b) in rectangles:
            mcd = gcd(a, b)
            
            x, y = a//mcd, b//mcd
            
            ans += counter[(x, y)]
            
            counter[(x, y)] += 1 
            
        return ans
        
                
                
                
                
                
