# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [2*(n - i - 1) for i in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(i - j)
                
                distIxyJ = abs(i - x + 1) + abs(j - y + 1) + 1
                distIyxJ = abs(i - y + 1) + abs(j - x + 1) + 1
                
                minDist = min(distIxyJ, distIyxJ)
                
                if minDist < dist: 
                    ans[dist - 1] -= 2
                    ans[minDist - 1] += 2 
                
        return ans 
        
