# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for (i, t) in enumerate(temperatures):
            while stack and stack[-1][0] < t: 
                (elem, idx) = stack.pop()
                ans[idx] = i - idx
                
            stack.append((t, i))
            
        return ans
            
