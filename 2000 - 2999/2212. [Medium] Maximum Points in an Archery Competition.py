# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ans = (0, [0 for i in range(12)])
        for i in range(2**12):
            arrows = [0 for i in range(12)]
            totalArrows = 0 
            points = 0 
            
            for j in range(12):
                bit = (i >> j) & 1
                if bit == 1: 
                    arrows[j] = aliceArrows[j] + 1
                    totalArrows += aliceArrows[j] + 1
                    points += j
            
            if totalArrows <= numArrows: 
                ans = max(ans, (points, arrows.copy()))
                
        ans = ans[1]
        aux = numArrows - sum(ans)
        
        for i in range(12):
            if ans[i] > aliceArrows[i]:
                ans[i] += aux
                break
                
        return ans 
