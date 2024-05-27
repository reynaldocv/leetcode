# https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        stack = [start]
        seen = {start}
        
        ans = 0 
        
        while stack: 
            newStack = []
            
            for x in stack:                 
                if x == goal: 
                    return ans 
                
                if 0 <= x <= 1000: 
                
                    for num in nums: 
                        for value in [x + num, x - num, x^num]:
                            if value not in seen: 
                                seen.add(value)
                            
                                newStack.append(value)            
                            
            ans += 1             
            stack = newStack
                           
        return -1 
                            

                
            
        
        
