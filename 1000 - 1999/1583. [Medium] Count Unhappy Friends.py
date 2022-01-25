# https://leetcode.com/problems/count-unhappy-friends/

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0 for _ in range(n)] for _ in range(n)]
        
        for u in range(n):
            rank[u][u] = float('inf')
            for (idx, v) in enumerate(preferences[u]):
                rank[u][v] = idx + 1
               
        partner = {}
        for (a, b) in pairs: 
            partner[a], partner[b] = b, a
            
        unhappy = 0
        for (x, y) in partner.items():
            if rank[x][y] == 1:
                continue
                
            chosen = y
			
            end = preferences[x].index(y)
            for u in preferences[x][:end]:
                if rank[u][x] < rank[u][partner[u]]:
                    chosen = u
                    break
                    
            if chosen != y:
                unhappy += 1
                
        return unhappy
                
        
