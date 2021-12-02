# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.n = len(rects)
        self.areas = [0 for _ in range(self.n)]
        total = 0 
        
        for (i, (x0, y0, x1, y1)) in enumerate(rects):             
            area = (x1 - x0 + 1)*(y1 - y0 + 1)
            self.areas[i] = area if i == 0 else area + self.areas[i - 1]
            
            total += area
            
        for i in range(self.n):
            self.areas[i] /= total
        
    def pick(self) -> List[int]:
        rand = random.uniform(0, 1)
        idx = bisect_left(self.areas, rand)
        x = random.randint(self.rects[idx][0], self.rects[idx][2])
        y = random.randint(self.rects[idx][1], self.rects[idx][3])
        
        return [x, y]
