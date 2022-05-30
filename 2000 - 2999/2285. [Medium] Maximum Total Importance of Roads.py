# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        for (a, b) in roads: 
            counter[a] += 1 
            counter[b] += 1 
        
        arr = [counter[i] for i in range(n)]
        arr.sort()
        
        ans = 0 
        
        for (i, num) in enumerate(arr):
            ans += num*(i + 1)
            
        return ans 
        
