# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(lambda: 0)
        losers = defaultdict(lambda: 0)
        
        for (a, b) in matches: 
            winners[a] += 1 
            losers[b] += 1 
            
        ans = [[], []]
        
        for key in winners:
            if losers[key] == 0: 
                ans[0].append(key)
            
        for key in losers: 
            if losers[key] == 1: 
                ans[1].append(key)
            
                
        ans[0].sort()
        ans[1].sort()
        
        return ans 
