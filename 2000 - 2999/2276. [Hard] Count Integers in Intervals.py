# https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals:
    def __init__(self):
        self.cnt = 0 
        self.intervals = []

    def add(self, left: int, right: int) -> None:
        idx = bisect_left(self.intervals, (left, right))
        
        while idx < len(self.intervals) and self.intervals[idx][0] <= right: 
            start, end = self.intervals.pop(idx)
            self.cnt -= end - start + 1
            
            right = max(right, end)
            
        if idx > 0 and left <= self.intervals[idx - 1][1]: 
            start, end = self.intervals.pop(idx - 1)
            self.cnt -= end - start + 1
            
            left = start            
            right = max(right, end)
            
        self.cnt += right - left + 1
        
        insort(self.intervals, (left, right))

    def count(self) -> int:
        return self.cnt
        
# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
