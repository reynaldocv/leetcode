# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.array = [None]*n
        self.pointer = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey - 1] = value
        ans = []
        while self.pointer < self.n and self.array[self.pointer] != None:
            ans.append(self.array[self.pointer])
            self.pointer += 1
        
        return ans
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
