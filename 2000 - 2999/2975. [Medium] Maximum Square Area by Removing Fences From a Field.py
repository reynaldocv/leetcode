# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7 
        
        if m == n: 
            return pow(m - 1, 2, MOD)
        
        hFences.sort() 
        vFences.sort()
        
        hFences.insert(0, 1)
        hFences.append(m)
        
        vFences.insert(0, 1)
        vFences.append(n)
        
        counter = defaultdict(lambda: 0)
        
        lh = len(hFences)
        
        for i in range(1, lh):
            for j in range(i - 1, -1, -1):
                counter[hFences[i] - hFences[j]] += 1 
                
        lv = len(vFences)
        
        side = 0 
        
        for i in range(1, lv):
            for j in range(i - 1, -1, -1):
                tmp = vFences[i] - vFences[j]
                
                if tmp in counter: 
                    side = max(side, tmp)
                    
        return -1 if side == 0 else pow(side, 2, MOD)
                    
                    
        
