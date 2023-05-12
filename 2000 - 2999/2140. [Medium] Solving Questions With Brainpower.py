# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache 
        def helper(i):
            if i >= n: 
                return 0 
            
            else: 
                return max(helper(i + 1), questions[i][0] + helper(i + questions[i][1] + 1))
                           
        n = len(questions)
        
        return helper(0)
    
class Solution2:
    def mostPoints(self, questions: List[List[int]]) -> int:        
        n = len(questions)
        
        dp = [0 for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            end = i + questions[i][1] + 1
            
            dp[i] = questions[i][0]
            
            if end < n:                 
                dp[i] += dp[end]
                
            if i + 1 < n: 
                dp[i] = max(dp[i], dp[i + 1])
                
        return dp[0]
    
 class Solution3:
    def mostPoints(self, questions: List[List[int]]) -> int:        
        n = len(questions)
        
        dp = defaultdict(lambda: 0)
        
        for i in range(n - 1, -1, -1):
            end = i + questions[i][1] + 1
            
            dp[i] = questions[i][0] + dp[end]
            
            dp[i] = max(dp[i], dp[i + 1])
                
        return dp[0]
            
            
                           
                
            
            
                           
                          
        
        
