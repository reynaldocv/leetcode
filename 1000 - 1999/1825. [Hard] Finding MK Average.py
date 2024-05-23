# https://leetcode.com/problems/finding-mk-average/

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m 
        self.k = k 
        
        self.sorted = []
        self.nums = []      
        
    def addElement(self, num: int) -> None:
        if len(self.nums) == self.m: 
            value = self.nums.pop(0)
            
            idx = bisect_left(self.sorted, value)
            
            self.sorted.pop(idx)
                  
        insort(self.sorted, num)
            
        self.nums.append(num)
      
    def calculateMKAverage(self) -> int:
        if len(self.sorted) < self.m: 
            return -1
        
        aSum = sum(self.sorted[self.k: -self.k]) 
        
        return aSum//(self.m - 2*self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

   
