# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                aux = img[i][j]
                div = 1
                for (a, b) in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]:
                    x, y = i + a, j + b
                    if 0 <= x < n and 0 <= y < m: 
                        aux += img[x][y]
                        div += 1
                ans[i][j] = int(aux/div)
        return ans
                    
        
        
