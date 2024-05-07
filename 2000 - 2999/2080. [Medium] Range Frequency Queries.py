# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.index = defaultdict(lambda: [])
        
        for (ith, num) in enumerate(arr):
            self.index[num].append(ith)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.index: 
            return 0 
        
        else: 
            start = bisect_left(self.index[value], left)
            end = bisect_right(self.index[value], right)
            
            return end - start

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
