# https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker:
  
    def __init__(self, arr: List[int]):
        self.idx = defaultdict(lambda: [])
        
        for (i, num) in enumerate(arr):
            self.idx[num].append(i)
            
        self.numbers = list(self.idx.keys())
        
        self.numbers.sort(key = lambda item: -len(self.idx[item]))
      
    def query(self, left: int, right: int, threshold: int) -> int:
        for num in self.numbers:
            if len(self.idx[num]) < threshold: 
                return -1
            
            idxLeft = bisect_left(self.idx[num], left)
            idxRight = bisect_right(self.idx[num], right)
           
            if idxRight - idxLeft >= threshold: 
                return num
            
        return -1
        
# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
