# https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        arr = [(positions[i], healths[i], directions[i]) for i in range(n)]
        
        arr.sort(key = lambda item: item[0])
        
        stack = []
        
        for (x, health, direction) in arr: 
            cur = health
            
            if direction == "L":
                while stack and stack[-1][2] == "R" and stack[-1][1] < cur:
                    stack.pop() 
                    
                    cur -= 1 
                    
                if stack and stack[-1][2] == "R": 
                    if stack[-1][1] > cur: 
                        (_x, _health, _direction) = stack.pop() 
                        
                        stack.append((_x, _health - 1, _direction))
                        
                    else: 
                        stack.pop()
                        
                else: 
                    stack.append((x, cur, direction))
            
            else: 
                stack.append((x, health, direction))
                
        value = {x: health for (x, health, _) in stack}
        
        ans = []
        
        for x in positions: 
            if x in value: 
                ans.append(value[x])
                
        return ans 
        
