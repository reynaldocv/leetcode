# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        seen = defaultdict(lambda: 0)
        
        for (start, end) in intervals: 
            seen[start] += 1 
            seen[end + 1] -= 1 
            
        coordX = [key for key in seen]
        coordX.sort() 
        
        prev = 0 
        ans = 0 
        
        for x in coordX: 
            prev += seen[x]
            ans = max(ans, prev)
        
        return ans 
