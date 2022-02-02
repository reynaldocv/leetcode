# https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree:

    def __init__(self):
        self.counter = defaultdict(lambda: 0)
        
    def book(self, start: int, end: int) -> int:
        self.counter[start] += 1 
        self.counter[end] -= 1 
        if self.counter[end] == 0: 
            self.counter.pop(end)
        
        arr = [key for key in self.counter]
        arr.sort()
        
        prev = ans = 0 
        for x in arr: 
            prev += self.counter[x]
            ans = max(ans, prev)
            
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
