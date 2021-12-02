# https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = rooms[0]
        visited = {0: True}
        
        while len(keys) > 0: 
            key = keys.pop()
            if key not in visited: 
                keys.extend(rooms[key])
                visited[key] = True
        
        return len(visited) == len(rooms)
        
