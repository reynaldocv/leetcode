# https://leetcode.com/problems/largest-submatrix-with-rearrangements/submissions/

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0 
        
        matrix.insert(0, [0 for _ in range(n)])
        
        for i in range(1, m + 1):        
            seen = defaultdict(lambda: 0)
            for j in range(n):
                if matrix[i][j] != 0: 
                    matrix[i][j] += matrix[i - 1][j]
                    seen[matrix[i][j]] += 1 
                    
            values = sorted([key for key in seen], reverse = True)
            
            witdh = 0 
            for val in values: 
                witdh += seen[val]
                ans = max(ans, witdh*val)
                
        return ans
