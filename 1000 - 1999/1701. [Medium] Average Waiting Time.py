# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        
        last = -inf 
        
        aSum = 0         
              
        for (arrival, time) in customers: 
            start = max(last, arrival)
            
            aSum += (start + time - arrival)
            
            last = start + time
            
        return aSum/n
        
        
        
