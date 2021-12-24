# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.values = defaultdict(lambda:[])
        self.times = defaultdict(lambda:[])

    def set(self, key: str, value: str, timestamp: int) -> None:
        idx = bisect_left(self.times[key], timestamp)
        
        self.times[key].insert(idx, timestamp)
        self.values[key].insert(idx, value)
        
    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_left(self.times[key], timestamp)
        if idx == 0:
            if not self.times[key] or timestamp < self.times[key][0]:
                return ""
        
        elif idx == len(self.times[key]) or self.times[key][idx] != timestamp:
            idx -= 1
        
        return self.values[key][idx]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
