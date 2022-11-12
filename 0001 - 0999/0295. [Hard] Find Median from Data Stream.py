# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0 

    def addNum(self, num: int) -> None:
        insort(self.arr, num)
        self.n += 1 

    def findMedian(self) -> float:
        mid = self.n // 2 
        if self.n % 2 == 1: 
            return self.arr[mid]
        else: 
            return (self.arr[mid - 1] +self.arr[mid])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
