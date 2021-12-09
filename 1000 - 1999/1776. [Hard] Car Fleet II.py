# https://leetcode.com/problems/car-fleet-ii/

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1 for _ in range(n)]
        
        stack = []
        
        cars = cars[::-1]
        
        for (i, (x, v)) in enumerate(cars):
            while stack and (v <= stack[-1][1] or (stack[-1][0] - x)/(v - stack[-1][1]) >= stack[-1][2]):
                stack.pop()
             
            if stack: 
                t = (stack[-1][0] - x)/(v - stack[-1][1])
                stack.append((x, v, t))
                ans[~i] = t
                
            else: 
                stack.append((x, v, inf))
             
        return ans
