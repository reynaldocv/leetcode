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
                           
                          
        
        
