# https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers:

    def __init__(self):
        self.listIdx = defaultdict(lambda: [])
        self.number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.number:
            num = self.number[index]
            
            idx = bisect_left(self.listIdx[num], index)
            
            self.listIdx[num].pop(idx)     
            
            if len(self.listIdx[num]) == 0: 
                self.listIdx.pop(num)
        
        self.number[index] = number 

        insort(self.listIdx[number], index)


    def find(self, number: int) -> int:
        if number in self.listIdx: 
            return self.listIdx[number][0]
        
        return -1 
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
