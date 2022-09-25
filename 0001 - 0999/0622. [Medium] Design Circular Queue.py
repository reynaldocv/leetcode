# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.total = k        
        self.idx = 0
        self.arr = []
        
    def enQueue(self, value: int) -> bool:
        if self.idx < self.total:
            self.arr.append(value)
            self.idx += 1 
            
            return True 
        
        return False 

    def deQueue(self) -> bool:
        if self.idx > 0: 
            self.idx -= 1 
            self.arr.pop(0) 
            
            return True 
        
        return False 
        
    def Front(self) -> int:
        if self.idx > 0:
            return self.arr[0]
        
        return -1 

    def Rear(self) -> int:
        if self.idx > 0: 
            return self.arr[self.idx - 1]
        
        return -1

    def isEmpty(self) -> bool:
        return self.idx == 0

    def isFull(self) -> bool:
        return self.idx == self.total

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
