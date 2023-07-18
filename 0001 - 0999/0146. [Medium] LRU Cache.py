# https://leetcode.com/problems/lru-cache/

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        ans = self.cache.get(key, -1)
        
        if ans != -1:             
            self.cache.move_to_end(key)
            
        return ans
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            
        elif len(self.cache) < self.capacity: 
            self.cache[key] = value
        
        else:
            self.cache[key] = value
        
            self.cache.popitem(0)
            
        self.cache.move_to_end(key)
                    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
