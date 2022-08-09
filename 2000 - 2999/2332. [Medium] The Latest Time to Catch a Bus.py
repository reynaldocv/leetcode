# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/submissions/

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort() 
        
        heapify(passengers) 
        
        users = []
        counter = []
        
        for bus in buses: 
            cnt = 0 
            while passengers and passengers[0] <= bus and cnt < capacity: 
                users.append(heappop(passengers))
                cnt += 1
                
            counter.append(cnt)
            
        ans = users[-1] if counter[-1] == capacity else buses[-1]
        
        users = {elem for elem in users}        
        
        while ans in users: 
            ans -= 1 
            
        return ans
