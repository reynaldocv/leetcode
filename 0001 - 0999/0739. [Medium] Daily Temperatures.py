# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        
        ans = [0 for _ in range(n)]
        
        for (i, temperature) in enumerate(temperatures):
            while stack and stack[-1][0] < temperature: 
                (_, idx) = stack.pop() 
                
                ans[idx] = i - idx 
                
            stack.append((temperature, i))
            
        return ans 
            
