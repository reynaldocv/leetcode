# https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda item: item[0])
        
        rooms = []
        
        for i in range(n):
            heappush(rooms, i)
            
        occupied = []
        
        counter = defaultdict(lambda: 0)
        
        for (start, end) in meetings:             
            while occupied and occupied[0][0] <= start: 
                (_, room) = heappop(occupied)
                
                heappush(rooms, room)
                
            if rooms: 
                room = heappop(rooms)

                counter[room] += 1 

                heappush(occupied, (end, room))
                
            else:                 
                (last, room) = heappop(occupied)
               
                counter[room] += 1 

                heappush(occupied, (last + end - start, room))

        ans = max((counter[key], -key) for key in counter)
        
        return -ans[1]
