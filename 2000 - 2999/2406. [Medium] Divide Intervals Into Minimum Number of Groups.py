# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        
        for (start, end) in intervals: 
            counter[start] += 1 
            counter[end + 1] -= 1 
            
        arr = sorted([key for key in counter])

        ans = prev = 0 
        
        for x in arr: 
            prev += counter[x]
            
            ans = max(ans, prev)
            
        return ans 
