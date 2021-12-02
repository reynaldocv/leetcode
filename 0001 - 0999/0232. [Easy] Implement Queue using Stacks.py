# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.n = 0
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.arr.insert(0, x)
        self.n += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        ans = self.arr.pop()
        self.n -= 1
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.arr[self.n - 1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.n == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
