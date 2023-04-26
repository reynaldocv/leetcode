# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.arr = ["" for _ in range(n)]
        self.idx = 0
        self.n = n 

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        
        ans = []
        
        while self.idx < self.n and self.arr[self.idx] != "":
            ans.append(self.arr[self.idx])
            
            self.idx += 1 
            
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
