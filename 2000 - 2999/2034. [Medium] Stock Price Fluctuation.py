# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice:

    def __init__(self):
        self.prices = OrderedDict()
        self.last = None
        self.maxHeap = []
        heapify(self.maxHeap)
        self.minHeap = []
        heapify(self.minHeap)
        
    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.last = max(self.last, timestamp) if self.last != None else timestamp
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.last]        

    def maximum(self) -> int:
        while (self.prices[self.maxHeap[0][1]] != -1*self.maxHeap[0][0]):
            heappop(self.maxHeap)
        return -1*self.maxHeap[0][0]

        
    def minimum(self) -> int:
        while (self.prices[self.minHeap[0][1]] != self.minHeap[0][0]):
            heappop(self.minHeap)
        return self.minHeap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
