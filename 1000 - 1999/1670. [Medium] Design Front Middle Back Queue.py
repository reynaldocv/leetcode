# https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = []
        self.len = 0 

    def pushFront(self, val: int) -> None:
        self.arr.insert(0, val)
        self.len += 1

    def pushMiddle(self, val: int) -> None:
        self.arr.insert(self.len//2, val)
        self.len += 1
        
    def pushBack(self, val: int) -> None:
        self.arr.append(val)
        self.len += 1
        
    def popFront(self) -> int:
        if self.len > 0: 
            self.len -= 1
            return self.arr.pop(0)
        
        return -1

    def popMiddle(self) -> int:
        if self.len > 0: 
            self.len -= 1        
            return self.arr.pop((self.len)//2)
        
        return -1
        
    def popBack(self) -> int:
        if self.len > 0: 
            self.len -= 1
            return self.arr.pop()
        
        return -1

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
