# https://leetcode.com/problems/range-module/

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:        
        idx = bisect_left(self.intervals, (left, inf))
        
        if idx > 0 and self.intervals[idx - 1][1] >= left:
            start = self.intervals[idx - 1][0]
            idx -= 1             
        else: 
            start = left
        
        while idx < len(self.intervals) and self.intervals[idx][1] <= right: 
            self.intervals.pop(idx)
            
        if idx < len(self.intervals):
            if self.intervals[idx][0] <= right: 
                end = self.intervals[idx][1]
                self.intervals.pop(idx)            
            else: 
                end = right
            insort(self.intervals, (start, end))
        else: 
            insort(self.intervals, (start, right))
        
    def queryRange(self, left: int, right: int) -> bool:        
        idx = bisect_left(self.intervals, (left, inf))
        
        if idx == 0:
            return False
        idx -= 1
        
        return self.intervals[idx][0] <= left and right <= self.intervals[idx][1]
        
    def removeRange(self, left: int, right: int) -> None:        
        idx = bisect_left(self.intervals, (left, inf))
        
        if idx > 0 and self.intervals[idx - 1][1] >= left:
            (start, end) = self.intervals.pop(idx - 1)
            if start < left:
                insort(self.intervals, (start, left))
                insort(self.intervals, (left, end))
            else:
                insort(self.intervals, (start, end))
                idx -= 1 
              
        while idx < len(self.intervals) and self.intervals[idx][1] <= right: 
            self.intervals.pop(idx)

        if idx < len(self.intervals):
            if self.intervals[idx][0] <= right: 
                (_, end) = self.intervals.pop(idx)            
                insort(self.intervals, (right, end))
        

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
