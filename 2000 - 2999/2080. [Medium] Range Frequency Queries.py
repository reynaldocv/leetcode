# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.seen = defaultdict(lambda: [])
        for (i, num) in enumerate(arr): 
            self.seen[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.seen: 
            return 0
        else: 
            arr = self.seen[value]
            start = bisect_left(arr, left)            
            end = bisect_right(arr, right)
            
            return end - start
        
                
                


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
