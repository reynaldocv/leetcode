# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0: 
                return a
            else: 
                return gcd(b, a % b)

        counter = {}
        for (w, h) in rectangles: 
            div = gcd(w, h)
            key = (w//div, h//div)
            counter[key] = counter.get(key, 0) + 1

        ans = 0 
        for key in counter: 
            if counter[key] > 1: 
                ans += counter[key]*(counter[key] - 1)//2

        return ans
                
                
                
                
                
