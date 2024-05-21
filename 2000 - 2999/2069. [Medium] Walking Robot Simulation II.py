# https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.ways = []
        self.directions = []
        
        self.total = 2*width + 2*height - 4
        
        self.position = 0
        
        self.moves = False
        
        for i in range(width):
            self.ways.append((i, 0))            
            self.directions.append("East")
            
        for j in range(1, height):
            self.ways.append((width - 1, j))            
            self.directions.append("North")
            
        for i in range(width - 2, -1, -1):
            self.ways.append((i, height - 1))            
            self.directions.append("West")
            
        for j in range(height - 2, 0, -1):
            self.ways.append((0, j))            
            self.directions.append("South")  
            
        self.directions[0] = "South"
    
    def step(self, num: int) -> None:
        self.moves = True 
        
        self.position = (self.position + num) % self.total
        
    def getPos(self) -> List[int]:
        return self.ways[self.position]        

    def getDir(self) -> str:
        if self.position == 0 and self.moves == False:
            return "East"
        
        else:
            return self.directions[self.position]
        
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
