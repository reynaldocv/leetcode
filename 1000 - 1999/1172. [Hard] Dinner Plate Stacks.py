# https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.stacks = []        
        self.minStacks = []

    def push(self, val: int) -> None:
        while self.minStacks: 
            ith = heappop(self.minStacks)
            
            if ith < len(self.stacks):
                break 
                
        else: 
            ith = len(self.stacks)
            
            self.stacks.append([])
            
        self.stacks[ith].append(val)
        
        if len(self.stacks[ith]) < self.capacity: 
            heappush(self.minStacks, ith)
       
    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop() 
            
        if self.stacks: 
            if len(self.stacks[-1]) == self.capacity: 
                heappush(self.minStacks, len(self.stacks) - 1)
                
            return self.stacks[-1].pop() 
        
        return -1         

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1 
        
        if len(self.stacks[index]) == self.capacity: 
            heappush(self.minStacks, index)
            
        return self.stacks[index].pop()
   
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)



