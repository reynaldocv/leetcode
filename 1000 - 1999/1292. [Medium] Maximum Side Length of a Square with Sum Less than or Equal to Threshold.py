# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def helper(i, j, r, s):
            return tmp[i][j] - tmp[r - 1][j] - tmp[i][s - 1] + tmp[r - 1][s - 1]
            
        m, n = len(mat), len(mat[0])
        
        tmp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                tmp[i + 1][j + 1] = tmp[i][j + 1] + tmp[i + 1][j] - tmp[i][j] + mat[i][j]
                
        ans = 0 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(min(i, j)):
                    if helper(i, j, i - k, j - k) <= threshold: 
                        ans = max(ans, k + 1)
                    else:
                        break
                        
        return ans
