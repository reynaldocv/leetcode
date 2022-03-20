# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        ans = 0 
        for direction in directions: 
            if direction == "L":
                if stack and stack[-1] == "R":
                    stack.pop()
                    stack.append("S")
                    ans += 2 
                else: 
                    stack.append(direction)                
            else: 
                stack.append(direction)
                
        directions = "".join(stack)
        
        cnt = 0 
        for direction in directions: 
            if direction == "S":
                ans += cnt
                cnt = 0
            elif direction == "R":
                cnt += 1
        
        cnt = 0 
        for direction in directions[::-1]: 
            if direction == "S":
                ans += cnt
                cnt = 0
            elif direction == "L":
                cnt += 1
        
        return ans
    
                        
                        
        
        
