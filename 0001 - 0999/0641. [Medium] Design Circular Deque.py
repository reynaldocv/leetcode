# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.n = 0 
        self.arr = []
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        if self.n < self.k:
            self.arr.insert(0, value)
            self.n += 1
            return True
        
        return False
        
    def insertLast(self, value: int) -> bool:
        if self.n < self.k:        
            self.arr.append(value)
            self.n += 1
            return True
        
        return False

    def deleteFront(self) -> bool:
        if self.n > 0: 
            self.arr.pop(0)
            self.n -= 1
            return True
        
        return False

    def deleteLast(self) -> bool:
        if self.n > 0: 
            self.arr.pop(self.n - 1)
            self.n -= 1
            return True
        
        return False

    def getFront(self) -> int:
        if self.n > 0: 
            return self.arr[0]
        
        return -1

    def getRear(self) -> int:
        if self.n > 0: 
            return self.arr[-1]
        
        return -1

    def isEmpty(self) -> bool:
        return self.n == 0 

    def isFull(self) -> bool:
        return self.n == self.k
        
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
