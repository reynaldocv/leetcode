# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        start = [(0, 0)]
        for i in range(1, n):
            start.append((i, 0))
        for j in range(1, m):
            start.append((n - 1, j))
        
        do = 1
        ans = []
        for (x, y) in start: 
            arr = [] 
            while 0 <= x < n and 0 <= y < m:
                arr.append(mat[x][y])
                x, y = x - 1, y + 1
            ans.extend(arr[::do])
            do *= -1
        
        return ans
                
                
            
            
            
        https://leetcode.com/problems/diagonal-traverse/
