# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.books = []
        
    def book(self, start: int, end: int) -> bool:
        n = len(self.books)
        if not self.books:
            insort(self.books, (start, end))
        else:
            idx = bisect_right(self.books, (start, end))
            if idx == len(self.books):
                if self.books[idx - 1][1] <= start:
                    insort(self.books, (start, end))
            elif idx == 0:
                if self.books[idx][0] >= end:
                    insort(self.books, (start, end))
            elif self.books[idx - 1][1] <= start:
                if self.books[idx][0] >= end: 
                    insort(self.books, (start, end))
        
        return n != len(self.books)
                    
            
            
        
        
