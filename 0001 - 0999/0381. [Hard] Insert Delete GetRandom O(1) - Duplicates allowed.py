# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.idx = defaultdict(lambda: set())
        
    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.arr))
        
        self.arr.append(val)
        
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        
        remove = self.idx[val].pop()
        last = self.arr[-1]
        
        self.arr[remove] = last
        
        self.idx[last].add(remove)
        self.idx[last].remove(len(self.arr) - 1)
        
        self.arr.pop()
        return True

    def getRandom(self) -> int:        
        return random.choice(self.arr)
        
# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
