# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        
        self.time = defaultdict(lambda: defaultdict(lambda: 0))
        self.counter = defaultdict(lambda: defaultdict(lambda: 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin: 
            (startStation, startTime) = self.checkin.pop(id)
            
            self.time[startStation][stationName] += (t - startTime)
            self.counter[startStation][stationName] += 1 
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.time and endStation in self.time[startStation]:
            return self.time[startStation][endStation]/self.counter[startStation][endStation] 
                        
        return 0 

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
