# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.dict = defaultdict(lambda: -1)

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        return self.dict[key]

    def remove(self, key: int) -> None:
        if key in self.dict: 
            self.dict.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
