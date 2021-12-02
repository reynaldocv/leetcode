# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def maxPointsOnALineContainingPoint(i):
            def slopeCoPrime(x1, y1, x2, y2):
                deltaX, deltaY = x1 - x2, y1 - y2

                if deltaX == 0: 
                    return (0, 0)

                elif deltaY == 0: 
                    return (inf, inf)

                elif deltaX < 0: 
                    deltaX, deltaY = -deltaX, -deltaY

                _gcd = gcd(deltaX, deltaY)

                return  (deltaX//_gcd, deltaY//_gcd)

            def addLine(i, j, count, duplicates):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2: 
                    duplicates += 1

                elif y1 == y2: 
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)

                else: 
                    slope = slopeCoPrime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)

                return count, duplicates


            lines, horizontal_lines = {}, 1
            count = 1
            duplicates = 0
            
            for j in range(i + 1, n):
                count, duplicates = addLine(i, j, count, duplicates)
                
            return count + duplicates
    
        maxCount = 1
        n = len(points)
        
        for i in range(n - 1):
            maxCount = max(maxPointsOnALineContainingPoint(i), maxCount)
            
        return maxCount
            
            
