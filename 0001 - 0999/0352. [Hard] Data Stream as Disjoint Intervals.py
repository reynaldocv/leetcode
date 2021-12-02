# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges:

    def __init__(self):
        self.nums = {}
        self.intervalS = {}
        self.intervalE = {}

    def addNum(self, val: int) -> None:
        if val not in self.nums: 
            self.nums[val] = val
            if val - 1 not in self.intervalE and val + 1 not in self.intervalS: 
                self.intervalS[val] = val
                self.intervalE[val] = val
                
            elif val - 1 in self.intervalE and val + 1 in self.intervalS:
                s = self.intervalE[val - 1]
                e = self.intervalS[val + 1]
                self.intervalE.pop(val - 1)
                self.intervalE.pop(e)
                self.intervalS.pop(val + 1)
                self.intervalS.pop(s)
                self.intervalS[s] = e
                self.intervalE[e] = s
                
            elif val - 1 in self.intervalE:
                s = self.intervalE[val - 1]
                self.intervalE.pop(val - 1)
                self.intervalS[s] = val
                self.intervalE[val] = s
            
            elif val + 1 in self.intervalS:
                e = self.intervalS[val + 1]
                self.intervalS.pop(val + 1)
                self.intervalS[val] = e
                self.intervalE[e] = val
                
    def getIntervals(self) -> List[List[int]]:
        ans = [(key, self.intervalS[key]) for key in self.intervalS]
        ans.sort()
        return ans
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
