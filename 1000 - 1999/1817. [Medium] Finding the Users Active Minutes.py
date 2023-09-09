# https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(lambda: set())
        
        for (idx, time) in logs: 
            counter[idx].add(time)
            
        ans = [0 for _ in range(k)]
        
        for key in counter:
            ans[len(counter[key]) - 1] += 1 
            
        return ans 
        
       
                
                
