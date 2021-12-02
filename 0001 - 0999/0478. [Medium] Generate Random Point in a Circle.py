# https://leetcode.com/problems/generate-random-point-in-a-circle/

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 2*pi)
        radio = self.r*sqrt(random.uniform(0,1))
        
        return [self.x + radio*cos(angle), self.y + radio*sin(angle)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
