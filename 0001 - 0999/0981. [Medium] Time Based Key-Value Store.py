# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.values = defaultdict(lambda: [])
        self.times = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.times[key], timestamp)
        
        idx -= 1 
        
        if idx >= 0: 
            return self.values[key][idx]
        
        return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
