# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        elems = defaultdict(lambda: [])
        
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                elems[i + j].append(mat[i][j]) 
                    
        ans = []                
         
        for i in range(m + n - 1):
            if i % 2 == 0: 
                ans.extend(elems[i][:: -1])
                
            else: 
                ans.extend(elems[i])
                
        return ans 
