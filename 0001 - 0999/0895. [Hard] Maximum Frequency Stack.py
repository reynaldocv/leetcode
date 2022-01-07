# https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(lambda: 0)
        self.group = defaultdict(lambda: [])
        self.maxFreq = 0
        
    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        
        if freq > self.maxFreq: 
            self.maxFreq = freq
            
        self.group[freq].append(val)
        
    def pop(self) -> int:        
        elem = self.group[self.maxFreq].pop()
        self.freq[elem] -= 1 
        
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        
        return elem

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
