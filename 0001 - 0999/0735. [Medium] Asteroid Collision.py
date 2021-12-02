# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids: 
            if asteroid > 0: 
                stack.append(asteroid)
            else: 
                add = True
                while stack and stack[-1] > 0: 
                    elem = stack.pop()   
                    if elem >= -asteroid: 
                        if elem > -asteroid: 
                            stack.append(elem)
                        add = False
                        break
                if add: 
                    stack.append(asteroid)
            
        return stack
                     
                        
                    
        
                    
