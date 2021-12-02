# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.n = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.arr.append(x)
        self.n += 1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        ans = self.arr[self.n - 1]
        self.arr.pop()
        self.n -= 1
        return ans

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.arr[self.n - 1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.n == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
