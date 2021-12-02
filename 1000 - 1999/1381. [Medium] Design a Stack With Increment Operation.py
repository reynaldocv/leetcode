# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.arr = []
        
    def push(self, x: int) -> None:
        if len(self.arr) < self.maxSize:
            self.arr.append(x)

    def pop(self) -> int:
        return self.arr.pop() if (len(self.arr) > 0) else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
