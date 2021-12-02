# https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
        
            return parents[x]
        
        def union(x,y):
            px, py = find(x), find(y)            
            parents[px] = parents[py] = min(px, py)
        
        timeStore = defaultdict(list)
        
        parents = [i for i in range(n)]
        
        for (x, y, t) in meetings:
            timeStore[t].append((x, y))
        
        union(0, firstPerson)
        
        for time in sorted(timeStore.keys()):            
            intermediate_seen = set()
            
            for (x, y) in timeStore[time]:
                union(x, y)                
                intermediate_seen.add(x)
                intermediate_seen.add(y)
            
            for x in intermediate_seen: 
                find(x)
                if parents[x] != 0:
                    parents[x] = x
        
        ans = []
        for i in range(n):
            if find(i) == 0:
                ans.append(i)
                
        return ans
