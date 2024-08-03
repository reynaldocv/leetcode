# https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        n = len(pick)
        
        counter = defaultdict(lambda: defaultdict(lambda: 0))
        
        for (x, y) in pick:
            counter[x][y] += 1 
            
        ans = 0
        
        for i in range(n):
            for key in counter[i]:
                if counter[i][key] > i: 
                    ans += 1 
                    
                    break 
        
        return ans
