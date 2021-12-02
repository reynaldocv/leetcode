# https://leetcode.com/problems/all-oone-data-structure/

class AllOne:

    def __init__(self):
        self.seen = defaultdict(lambda: 0)
        self.minHeap = []
        self.maxHeap = []

    def inc(self, key: str) -> None:
        self.seen[key] += 1
        heappush(self.minHeap, (self.seen[key], key))
        heappush(self.maxHeap, (-self.seen[key], key))

    def dec(self, key: str) -> None:
        if key in self.seen: 
            self.seen[key] -= 1
            if self.seen[key] <= 0: 
                del self.seen[key]
            else: 
                heappush(self.minHeap, (self.seen[key], key))
                heappush(self.maxHeap, (-self.seen[key], key))

    def getMaxKey(self) -> str:
        if self.seen: 
            while self.maxHeap and self.seen[self.maxHeap[0][1]] != -1*self.maxHeap[0][0]:
                heappop(self.maxHeap)
                
            return self.maxHeap[0][1]
        else: 
            return ""
    def getMinKey(self) -> str:
        if self.seen: 
            while self.minHeap and self.seen[self.minHeap[0][1]] != self.minHeap[0][0]:
                heappop(self.minHeap)
                
            return self.minHeap[0][1]
        else: 
            return ""
            
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
