# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.next = 1
        self.seen = set()

    def popSmallest(self) -> int:
        if self.heap: 
            elem = heappop(self.heap)
            self.seen.remove(elem)

            return elem        
            
        else: 
            self.next += 1 
            
            return self.next - 1             

    def addBack(self, num: int) -> None:
        if num < self.next and num not in self.seen:
            heappush(self.heap, num)
            self.seen.add(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
