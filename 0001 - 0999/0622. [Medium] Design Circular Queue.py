# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.n = 0 
        self.arr = []
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if self.n < self.k: 
            self.arr.append(value)
            self.n += 1
            return True
        
        return False

    def deQueue(self) -> bool:
        if self.n > 0: 
            self.arr.pop(0)
            self.n -= 1
            return True
        
        return False

    def Front(self) -> int:
        if self.n > 0: 
            return self.arr[0]
        
        return -1

    def Rear(self) -> int:
        if self.n > 0: 
            return self.arr[-1]
        
        return -1

    def isEmpty(self) -> bool:
        return self.n == 0
        

    def isFull(self) -> bool:
        return self.n == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
