# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.n = 0

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.n += 1
        

    def pop(self) -> None:
        if self.n >= 1: 
            self.arr.pop()
            self.n -= 1

    def top(self) -> int:
        if self.n >= 1:
            return self.arr[self.n - 1]
        

    def getMin(self) -> int:
        if (self.n) >= 1: 
            return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
