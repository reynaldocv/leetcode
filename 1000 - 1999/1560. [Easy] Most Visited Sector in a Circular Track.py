# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        m = len(rounds)
        i = rounds[0]
        j = rounds[m - 1]
        if i == j:
            ans = [i] 
        elif i < j: 
            ans = [x for x in range(i, j + 1)]
        else: 
            ans = []
            for x in range(1, n + 1):
                if x <= j or x >= i:
                    ans.append(x)
                
                
        return ans
        
