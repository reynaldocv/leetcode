# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers:

    def __init__(self):
        self.index = defaultdict(lambda: [])
        self.value = {}

    def change(self, index: int, number: int) -> None:
        if index in self.value:
        
            value = self.value[index]
            idx = bisect_left(self.index[value], index)
        
            if idx < len(self.index[value]):
                self.index[value].pop(idx)
            
        insort(self.index[number], index)
        
        self.value[index] = number

    def find(self, number: int) -> int:
        if not self.index[number]: 
            return -1
        
        else: 
            return self.index[number][0]
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
