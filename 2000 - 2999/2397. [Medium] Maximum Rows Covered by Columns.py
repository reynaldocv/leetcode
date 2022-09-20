# https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        
        index = defaultdict(lambda: set())
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    index[i].add(j)
                    
        ans = 0 
        
        for comb in combinations([i for i in range(n)], cols):
            cur = 0 
            
            comb = set(comb)
            
            for i in range(m):
                if not(index[i] - comb):
                    cur += 1 
                    
            ans = max(ans, cur)
            
        return ans 
