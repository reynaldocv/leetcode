# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        n, m = len(image), len(image[0])
        arr = [(sr, sc)]
        visited = {(sr, sc): False}
        while len(arr) > 0: 
            (i, j) = arr.pop()
            if visited[(i, j)] == False:
                visited[(i, j)] = True
                image[i][j] = newColor
                for (a, b) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x, y = i + a, j + b
                    if 0 <= x < n and 0<= y < m:
                        if image[x][y] == color and (x, y) not in visited : 
                            visited[(x, y)] = False
                            arr.append((x, y))
        return image
                    
                
