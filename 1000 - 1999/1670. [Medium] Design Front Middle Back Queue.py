# https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        n = len(self.arr)
        
        self.arr.insert(n//2, val)

    def pushBack(self, val: int) -> None:
        self.arr.append(val)

    def popFront(self) -> int:
        if self.arr:             
            return self.arr.pop(0)
        
        else: 
            return -1
        
    def popMiddle(self) -> int:
        n = len(self.arr)
        
        if n and n % 2 == 0:         
            return self.arr.pop(n//2 - 1)

        elif n and n % 2 == 1: 
            return self.arr.pop(n//2)
        
        return -1

    def popBack(self) -> int:
        if self.arr: 
            return self.arr.pop()
        
        else: 
            return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
