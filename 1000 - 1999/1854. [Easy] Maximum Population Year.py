# https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        for (start, end) in logs: 
            counter[start] += 1
            counter[end] -= 1 
            
        coordinates = [key for key in counter]
        
        coordinates.sort() 
        
        prev = 0 
        
        ans = (0, 0)
        
        for x in coordinates:
            prev += counter[x]
            
            print(x, prev)
            
            ans = max(ans, (prev, -x))
            
        return -ans[1]
        
