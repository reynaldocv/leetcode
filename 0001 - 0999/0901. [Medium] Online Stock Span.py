# https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        self.arr = []
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price: 
            self.stack.pop()
            
        self.arr.append(price)
        n = len(self.arr)        
        
        ans = n - self.stack[-1][1] if self.stack else n
        
        self.stack.append((price, n))
        
        return ans
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
