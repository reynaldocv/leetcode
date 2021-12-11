# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker:

    def __init__(self):
        self.arr = []
        self.idx = 0 

    def add(self, name: str, score: int) -> None:
        insort(self.arr, (-score, name))

    def get(self) -> str:
        self.idx += 1
        return self.arr[self.idx - 1][1]

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
