# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.coordX = {}
        

    def add(self, point: List[int]) -> None:
        (x, y) = point
        
        self.coordX[x] = self.coordX.get(x, {})
        self.coordX[x][y] = self.coordX[x].get(y, 0) + 1

    def count(self, point: List[int]) -> int:
        ans = 0
        (r, s) = point
        for x in self.coordX:
            if s in self.coordX[x]:
                dist = abs(x - r)
                if dist > 0: 
                    if s + dist in self.coordX[x] and r in self.coordX and s + dist in self.coordX[r]:
                        ans += self.coordX[x][s] * self.coordX[x][s + dist] * self.coordX[r][s + dist]
                    if s - dist in self.coordX[x] and r in self.coordX and s - dist in self.coordX[r]:
                        ans += self.coordX[x][s] * self.coordX[x][s - dist] * self.coordX[r][s - dist]

        return ans
                    
                    
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
