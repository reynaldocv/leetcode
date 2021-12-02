# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        print(n, m)
        ways = [[0 for _ in range(m)] for _ in range(n)]
        ways[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        for j in range(1, m):
            ways[0][j] +=  ways[0][j - 1] if obstacleGrid[0][j] == 0 else ways[0][j]
        
        for i in range(1, n):
            ways[i][0] +=  ways[i - 1][0] if obstacleGrid[i][0] == 0 else ways[i][0]
            
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0: 
                    ways[i][j] += ways[i - 1][j] + ways[i][j - 1]
                    
        return ways[-1][-1]
                    
        
        
        
