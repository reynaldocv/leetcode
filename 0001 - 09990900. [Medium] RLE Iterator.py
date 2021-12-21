# https://leetcode.com/problems/rle-iterator/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        prev = 0 
        n = len(encoding)
        self.index = []
        self.values = []
        for i in range(n//2):
            num = encoding[2*i]
            val = encoding[2*i + 1]
            if num != 0: 
                prev += num
                self.index.append(prev)
                self.values.append(val)
        
        self.nth = 0
        
    def next(self, n: int) -> int:
        self.nth += n 
        idx = bisect_left(self.index, self.nth)
        if idx == len(self.index):
            return -1
        else:
            return self.values[idx]
        
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
