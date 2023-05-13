# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def helper(x):
            nonlocal ans 
            total = 0 
            
            for v in graph[x]:
                if v not in seen: 
                    seen.add(v)
                    count = helper(v)
                    total += count
                    
                    if count % seats == 0: 
                        ans += count//seats

                    else: 
                        ans += count//seats + 1

            return total + 1

        graph = defaultdict(lambda: [])
        
        for (a, b) in roads: 
            graph[a].append(b)
            graph[b].append(a)
            
        seen = {0}
        
        ans = 0 
        
        helper(0)
        
        return ans 
