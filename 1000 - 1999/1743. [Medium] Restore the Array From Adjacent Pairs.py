# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(lambda: [])
        for (a, b) in adjacentPairs: 
            adjacents[a].append(b)
            adjacents[b].append(a)
            
        alones = [a for a in adjacents if len(adjacents[a]) == 1]
        
        ans = [alones[0]]
        seen = {alones[0]: True}
        
        while len(ans) != len(adjacentPairs) + 1: 
            u = ans[-1]
            for v in adjacents[u]:
                if v not in seen: 
                    seen[v] = True
                    ans.append(v)
                    
        return ans
        
