# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        seen = defaultdict(lambda: 0)
        for (idx, (x0, y0, x1, y1)) in enumerate(artifacts): 
            for i in range(x0, x1 + 1):
                for j in range(y0, y1 + 1):
                    seen[(i,j)] = idx + 1
                    counter[idx + 1] += 1
            
        cnt = defaultdict(lambda: 0)
            
        for (x, y) in dig: 
            cnt[seen[(x, y)]] += 1 
            
        ans = 0 
        for key in cnt: 
            if key != 0: 
                if cnt[key] == counter[key]:
                    ans += 1 
                    
        return ans
                
