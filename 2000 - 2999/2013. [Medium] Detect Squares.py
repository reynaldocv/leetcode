# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.abscissa = defaultdict(lambda: set([]))
        self.counter = defaultdict(lambda: 0)
        
    def add(self, point: List[int]) -> None:
        (x, y) = point
        
        self.abscissa[x].add(y)        
        self.counter[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        (x1, y1) = point
        
        ans = 0 
        
        for y2 in self.abscissa[x1]:
            side = abs(y2 - y1)
            
            if side > 0:            
                qnt = 1 
                qnt *= self.counter[(x1, y2)]
                qnt *= self.counter[(x1 + side, y1)]
                qnt *= self.counter[(x1 + side, y2)]

                ans += qnt

                qnt = 1 
                qnt *= self.counter[(x1, y2)]
                qnt *= self.counter[(x1 - side, y1)]
                qnt *= self.counter[(x1 - side, y2)]

                ans += qnt

        return ans 

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
