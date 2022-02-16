# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class MyCalendarTwo:

    def __init__(self):
        self.counter = defaultdict(lambda: 0)
        self.points = []
        self.seen = {}
        
    def book(self, start: int, end: int) -> bool:
        points = self.points.copy()
        seen = self.seen.copy()
        
        if start not in seen: 
            seen[start] = True
            insort(points, start)
        if end not in seen:
            seen[end] = True
            insort(points, end)
        
        self.counter[start] += 1 
        self.counter[end] -= 1 
        
        go = True 
        cnt = 0 
        
        for x in points: 
            cnt += self.counter[x]
            if cnt > 2: 
                go = False
                break
                
        if go: 
            self.points = points
            self.seen = seen
        else: 
            self.counter[start] -= 1 
            self.counter[end] += 1 
        
        return go 
            
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
