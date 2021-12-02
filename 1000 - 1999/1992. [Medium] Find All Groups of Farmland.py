# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def searchLimits(i, j):
            ii, jj = i, j
            while ii + 1 < n and land[ii + 1][j] == 1:
                ii += 1
            while jj + 1 < m and land[i][jj + 1] == 1: 
                jj += 1
            for a in range(i, ii + 1):
                for b in range(j, jj + 1):
                    land[a][b] = val 
            return ii, jj
                
        n, m = len(land), len(land[0])
        val = 0
        ans = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1: 
                    k, l = searchLimits(i, j)
                    ans.append([i, j, k, l])
                    
        return ans
                    
   
        
            
