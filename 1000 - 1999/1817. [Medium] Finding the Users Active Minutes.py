# https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        accessed = defaultdict(lambda: {})
        for (a, b) in logs: 
            accessed[a][b] = True
            
        ans = [0 for _ in range(k)]
        
        for user in accessed: 
            ans[len(accessed[user]) - 1] += 1 
            
        return ans
       
                
                
