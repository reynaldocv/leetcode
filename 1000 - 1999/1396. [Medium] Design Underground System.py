# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.total = defaultdict(lambda: [])
        self.checkin = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (start, t0) = self.checkin[id]
        self.checkin.pop(id)
        self.total[(start, stationName)].append(t - t0)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        n = len(self.total[(startStation, endStation)])
        return sum(self.total[(startStation, endStation)])/n
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
