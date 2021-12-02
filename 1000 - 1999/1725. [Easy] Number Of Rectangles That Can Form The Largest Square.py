# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = {}
        ans = 0
        for rectangle in rectangles:
            l = min(rectangle)
            squares[l] = squares.get(l, 0) + 1
            ans = max(ans, l)
        return squares[ans]
