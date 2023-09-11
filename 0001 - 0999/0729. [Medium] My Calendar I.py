# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        idx1 = bisect_left(self.starts, end)
        idx2 = bisect_right(self.ends, start)
        
        if idx1 == idx2: 
            self.starts.insert(idx1, start)
            self.ends.insert(idx2, end)
            
            return True 
        
        return False 
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
                    
            
            
        
        
