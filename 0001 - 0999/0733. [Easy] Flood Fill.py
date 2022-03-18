# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        
        color = image[sr][sc]
        stack = [(sr, sc)]
        seen = {(sr, sc): True}
        
        image[sr][sc] = newColor
        
        while stack: 
            (x, y) = stack.pop()
            for (r, s) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                p, q = x + r, y + s
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen and image[p][q] == color: 
                        seen[(p, q)] = True
                        image[p][q] = newColor
                        stack.append((p, q))
                        
        return image
                    
                
