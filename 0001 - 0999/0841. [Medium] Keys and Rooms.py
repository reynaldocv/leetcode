# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        seen = {0}        
        stack = [0]
        
        while stack: 
            x = stack.pop()
            
            for y in rooms[x]:
                if y not in seen: 
                    seen.add(y)
                    
                    stack.append(y)
                    
        return len(seen) == n
        
        
        
