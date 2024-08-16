# https://leetcode.com/problems/all-oone-data-structure/

class AllOne:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
        self.counter = defaultdict(lambda: 0)

    def inc(self, key: str) -> None:
        self.counter[key] += 1 
        
        heappush(self.maxHeap, (-self.counter[key], key))
        heappush(self.minHeap, (self.counter[key], key))
        
    def dec(self, key: str) -> None:        
        self.counter[key] -= 1 
        
    def getMaxKey(self) -> str:        
        while self.maxHeap and self.counter[self.maxHeap[0][1]] != -self.maxHeap[0][0] :
            heappop(self.maxHeap)
        
        if self.maxHeap: 
            return self.maxHeap[0][1]
        
        else: 
            return ""
        
    def getMinKey(self) -> str:
        while self.minHeap and self.counter[self.minHeap[0][1]] != self.minHeap[0][0]:
            heappop(self.minHeap)
        
        if self.minHeap: 
            return self.minHeap[0][1]
        
        else: 
            return ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

