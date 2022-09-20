# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m, n = len(players), len(trainers)
        
        players.sort()
        trainers.sort()
        
        ans = 0 
        
        i, j = 0, 0 
        
        while i < m and j < n: 
            if players[i] <= trainers[j]:
                ans += 1 
                i += 1 
                j += 1 
            else:
                j += 1 
                
        return ans 
        
