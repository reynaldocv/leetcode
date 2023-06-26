# https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker:

    def __init__(self):
        self.frequency = {}        
        self.numbers = defaultdict(lambda: set())

    def add(self, number: int) -> None:
        if number not in self.frequency: 
            self.frequency[number] = 1 
            
            self.numbers[1].add(number)
        
        else: 
            freq = self.frequency[number]
            
            self.numbers[freq].remove(number)
            self.numbers[freq + 1].add(number)
            
            self.frequency[number] += 1 
            
    def deleteOne(self, number: int) -> None:
        if number in self.frequency: 
            freq = self.frequency[number]
            
            self.numbers[freq].remove(number)
                
            if freq == 1:             
                self.frequency.pop(number)
                
            else:                 
                self.numbers[freq - 1].add(number)
                
                self.frequency[number] -= 1 
                
    def hasFrequency(self, frequency: int) -> bool:
        return len(self.numbers[frequency]) > 0        

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
