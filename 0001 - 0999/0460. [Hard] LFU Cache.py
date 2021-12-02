# https://leetcode.com/problems/lfu-cache/

class LFUCache:

    def __init__(self, capacity: int):
        self.freq_map = defaultdict(lambda: {})
        self.min_freq = None
        self.capacity = capacity
        self.cache = {}
        
    def updateFrequenciesAndCache(self, oldFreq, key, val):
        self.cache[key] = (val, oldFreq + 1)
        self.freq_map[oldFreq].pop(key)
        self.freq_map[oldFreq + 1][key] = val
        
        if self.min_freq == oldFreq and not self.freq_map[oldFreq]:
            self.min_freq = oldFreq + 1 
            
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        (val, freq) = self.cache[key]
        self.updateFrequenciesAndCache(freq, key, val)

        return val
                   
        
    def put(self, key: int, value: int) -> None:       
        
        if not self.capacity:   
            return
        
        if key in self.cache:
            (oldVal, freq) = self.cache[key]
            self.updateFrequenciesAndCache(freq, key, value)
        else:
            if len(self.cache) == self.capacity:
                arr = self.freq_map[self.min_freq]
                oldKey = next(iter(arr))
                
                self.freq_map[self.min_freq].pop(oldKey)
                self.cache.pop(oldKey)

            newFreq = 1
            self.cache[key] = (value, newFreq)
            self.freq_map[newFreq][key] = value
            if not self.min_freq or newFreq < self.min_freq:
                self.min_freq = newFreq
            
            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
