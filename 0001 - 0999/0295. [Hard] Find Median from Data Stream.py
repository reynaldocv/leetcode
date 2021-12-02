# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        idx = bisect_left(self.arr, num)
        self.arr.insert(idx, num)
        self.n += 1
        
    def findMedian(self) -> float:
        m = self.n//2
        if self.n % 2 == 1:
            return self.arr[m]
        else: 
            return (self.arr[m - 1] + self.arr[m])/2
        
