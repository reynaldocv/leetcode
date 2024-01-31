# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        
        stack = [(inf, -1)]
        
        ans = [0 for _ in range(n)]
        
        for (i, temp) in enumerate(temperatures):
            while stack[-1][0] < temp: 
                (_, idx) = stack.pop()
                
                ans[idx] = i - idx
                
            stack.append((temp, i))
            
        return ans 
        
        
            
