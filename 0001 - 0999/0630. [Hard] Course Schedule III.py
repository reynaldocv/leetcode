# https://leetcode.com/problems/course-schedule-iii/

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        prefix = 0 
        
        heap = [] 
        courses.sort(key = lambda item: item[1])
        
        for (x, y) in courses: 
            prefix += x
            heappush(heap, -x) 
            
            while prefix > y: 
                prefix += heappop(heap)
                
        return len(heap)
        
