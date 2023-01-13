# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def helper(x, y):
            ans = 0 
            
            cnt = 0 
            
            for i in [x - 1, x, x + 1]:
                for j in [y - 1, y, y + 1]:
                    if 0 <= i < m and 0 <= j < n: 
                        ans += img[i][j]
                        cnt += 1 
                        
            return ans//cnt
                    
        m, n = len(img), len(img[0])
        
        return [[helper(i, j) for j in range(n)] for i in range(m)]
             
                    
