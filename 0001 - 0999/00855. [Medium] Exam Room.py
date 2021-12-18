# https://leetcode.com/problems/exam-room/

class ExamRoom:

    def __init__(self, n: int):
        self.occupied = []
        self.n = n
        
    def seat(self) -> int:
        if not self.occupied:
            self.occupied.append(0)
            return 0 
        
        left, right = -self.occupied[0], self.occupied[0]
        maximum = (right - left)//2
        
        for (i, start) in enumerate(self.occupied): 
            if i + 1 == len(self.occupied):
                end = 2*self.n - 2 - self.occupied[-1]
            else:
                end = self.occupied[i + 1]
                
            space = (end - start)//2
            if space > maximum: 
                left = start 
                maximum = space
    
        insort(self.occupied, left + maximum)
        
        return left + maximum
    
    def leave(self, p: int) -> None:
        idx = bisect_left(self.occupied, p)
        
        self.occupied.pop(idx)
        
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
