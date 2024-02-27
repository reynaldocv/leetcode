# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        
        ans = 0 
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                maxXBottomLeft = max(bottomLeft[i][0], bottomLeft[j][0])
                minXTopRight = min(topRight[i][0], topRight[j][0])
                
                maxYBottomLeft = max(bottomLeft[i][1], bottomLeft[j][1])
                minYTopRight = min(topRight[i][1], topRight[j][1])
                
                if maxXBottomLeft < minXTopRight and maxYBottomLeft < minYTopRight: 
                    side = min(minXTopRight - maxXBottomLeft, minYTopRight - maxYBottomLeft)
                    ans = max(ans, side**2)
                        
        return ans 
                    
                
