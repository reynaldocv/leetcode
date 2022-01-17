# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = defaultdict(lambda: 0)
        ans = 0 
        
        for (i, (points, nextDays)) in enumerate(questions):
            memo[i] = max(memo[i - 1], memo[i])
            
            val = memo[i] + points            
            memo[i + nextDays + 1] = max(memo[i + nextDays + 1], val)
            
            ans = max(ans, val)   
            
        return ans
        
        
