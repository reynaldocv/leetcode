# https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.seen = {i: True for i in range(1, 1001)}
        self.heap = [i for i in range(1, 1001)]
        
        heapify(self.heap)
        
    def popSmallest(self) -> int:
        ans = heappop(self.heap)
        self.seen.pop(ans)
        
        return ans
    
    def addBack(self, num: int) -> None:
        if num not in self.seen:
            heappush(self.heap, num)
            self.seen[num] = True

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
