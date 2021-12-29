# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seen = defaultdict(lambda: 0)
        for (persons, origin, destiny) in trips: 
            seen[origin] += persons
            seen[destiny] -= persons
            
        points = [key for key in seen]
        points.sort()
        
        total = 0 
        for x in points:
            total += seen[x]
            if total > capacity: 
                return False
            
        return True
            
            
            
