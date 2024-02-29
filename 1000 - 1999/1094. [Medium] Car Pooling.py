# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = defaultdict(lambda: 0)
        
        for (passengers, start, end) in trips: 
            counter[start] += passengers
            
            counter[end] -= passengers
            
        arr = [key for key in counter]        
        arr.sort() 
        
        total = 0 
        
        for num in arr: 
            total += counter[num]
            
            if total > capacity: 
                return False 
            
        return True 
        
            
            
            
