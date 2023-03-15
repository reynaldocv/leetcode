# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: 
            return image
        
        n, m = len(image), len(image[0])
        
        oldColor = image[sr][sc]
        
        stack = [(sr, sc)]
        image[sr][sc] = color
        
        while stack: 
            (x, y) = stack.pop() 
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < n and 0 <= q < m and (p, q):
                    if image[p][q] == oldColor: 
                        image[p][q] = color
                    
                        stack.append((p, q))
            
        return image    
            
            
                
