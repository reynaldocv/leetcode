# https://leetcode.com/problems/design-bitset/

class Bitset:

    def __init__(self, size: int):
        self.n = size
        self.bit = {}
        self.flipp = True        

    def fix(self, idx: int) -> None:
        if idx < self.n: 
            if self.flipp:                 
                self.bit[idx] = True
            elif idx in self.bit: 
                self.bit.pop(idx)
            
    def unfix(self, idx: int) -> None:
        if idx < self.n:
            if self.flipp:
                if idx in self.bit: 
                    self.bit.pop(idx)
            else: 
                self.bit[idx] = True 

    def flip(self) -> None:
        self.flipp = not self.flipp

    def all(self) -> bool:
        if self.flipp:
            return len(self.bit) == self.n
        else: 
            return len(self.bit) == 0 

    def one(self) -> bool:
        if self.flipp:
            return len(self.bit) > 0 
        else: 
            return len(self.bit) < self.n

    def count(self) -> int:
        if self.flipp: 
            return len(self.bit)
        else: 
            return self.n - len(self.bit)

    def toString(self) -> str:
        ans = "" 
        if self.flipp:             
            for i in range(self.n):
                ans += "1" if i in self.bit else "0"
        else: 
            for i in range(self.n):
                ans += "0" if i in self.bit else "1"
        
        return ans

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
