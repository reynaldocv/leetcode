# https://leetcode.com/problems/fancy-sequence/

class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        
        self.arr = []
        self.mul = [1]   
        self.sum = [0]             

    def append(self, val: int) -> None:
        self.arr.append(val)
        self.sum.append(self.sum[-1])
        self.mul.append(self.mul[-1])
        
    def addAll(self, inc: int) -> None:
        self.sum[-1] += inc        

    def multAll(self, m: int) -> None:        
        self.sum[-1] = (self.sum[-1] * m) % self.MOD
        self.mul[-1] = (self.mul[-1] * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx < len(self.arr): 
            power = pow(self.mul[idx], -1, self.MOD)
            
            ratio = self.mul[-1]*power
            
            ans = ((self.arr[idx] - self.sum[idx])*ratio + self.sum[-1]) % self.MOD
            
            return ans 
        
        return -1 

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
