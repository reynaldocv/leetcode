# https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice:

    def __init__(self):
        self.times = []
        self.prices = []
        
        self.counter = defaultdict(lambda: 0)
        
        self.maxHeap = []
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        idx = bisect_left(self.times, timestamp)
        
        if idx < len(self.times):
            if self.times[idx] == timestamp: 
                oldPrice = self.prices[idx]                
                self.counter[oldPrice] -= 1 
                                                 
                self.prices[idx] = price                
                self.counter[price] += 1             
                
            else: 
                self.times.insert(idx, timestamp)
                self.prices.insert(idx, price)
                
                self.counter[price] += 1 
                
        else: 
            self.times.append(timestamp)
            self.prices.append(price)
            
            self.counter[price] += 1 
            
        heappush(self.maxHeap, -price)
        heappush(self.minHeap, price)

    def current(self) -> int:
        if self.prices: 
            return self.prices[-1]
        
        return -1 

    def maximum(self) -> int:
        while self.maxHeap and self.counter[-self.maxHeap[0]] == 0: 
            heappop(self.maxHeap)
            
        if self.maxHeap: 
            return -self.maxHeap[0]
        
        return -1 
    
    def minimum(self) -> int:
        while self.minHeap and self.counter[self.minHeap[0]] == 0: 
            heappop(self.minHeap)
            
        if self.minHeap: 
            return self.minHeap[0]
        
        return -1 
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
