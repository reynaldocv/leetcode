# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = {0: True}
        
        stack = [0]
        
        while stack: 
            u = stack.pop()
            for key in rooms[u]:
                if key not in seen: 
                    seen[key] = True 
                    stack.append(key)
                    
        return len(seen) == n
        
        
