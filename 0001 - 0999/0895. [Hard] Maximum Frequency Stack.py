# https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.counter = defaultdict(lambda: 0)        
        self.stacks = defaultdict(lambda: [])
        
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        
        self.stacks[self.counter[val]].append(val)
        
        self.maxFreq = max(self.maxFreq, self.counter[val])

    def pop(self) -> int:        
        elem = self.stacks[self.maxFreq].pop()
        
        self.counter[elem] -= 1 
        
        if len(self.stacks[self.maxFreq]) == 0:
            self.stacks.pop(self.maxFreq)
        
            self.maxFreq -= 1 
            
        return elem

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
