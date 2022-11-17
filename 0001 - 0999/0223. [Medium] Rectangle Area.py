# https://leetcode.com/problems/rectangle-area/

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def helper(ax, ay, bx, by):
            return abs(bx - ax)*abs(by - ay)
        
        ans = helper(ax1, ay1, ax2, ay2) + helper(bx1, by1, bx2, by2)
        
        if not(ax2 <= bx1 or bx2 <= ax1 or by2 <= ay1 or ay2 <= by1): 
            cx1 = max(ax1, bx1)
            cy1 = max(ay1, by1)
            cx2 = min(ax2, bx2)
            cy2 = min(ay2, by2)
            
            ans -= helper(cx1, cy1, cx2, cy2)
            
        return ans 
            
       
