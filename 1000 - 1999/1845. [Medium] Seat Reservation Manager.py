# https://leetcode.com/problems/seat-reservation-manager/

class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.free = {i: False for i in range(1, n + 1)}
        self.heap = [i for i in range(1, n + 1)]
        
        heapify(self.heap)
        
        

    def reserve(self) -> int:
        while self.heap and self.free[self.heap[0]] == True: 
            heappop(heap)
            
        if self.heap: 
            elem = heappop(self.heap)
            self.free[elem] = True
            return elem
        
    def unreserve(self, seatNumber: int) -> None:
        self.free[seatNumber] = False
        heappush(self.heap, seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
