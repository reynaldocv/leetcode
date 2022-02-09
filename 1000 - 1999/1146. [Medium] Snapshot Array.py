# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.cache = [[[-1, 0]] for _ in range(length)]
        self.idx = 0 

    def set(self, index: int, val: int) -> None:
        self.cache[index].append([self.idx, val])

    def snap(self) -> int:
        self.idx += 1 
        return self.idx - 1
    
    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_left(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][idx][1]
        
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


