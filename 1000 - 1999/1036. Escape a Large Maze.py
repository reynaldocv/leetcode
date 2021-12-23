# https://leetcode.com/problems/escape-a-large-maze/ 

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def helper(x, y, x_, y_):
            seen = {(x, y): True}
            stack = [(x, y)]
            lvl = 0 
            while stack: 
                lvl += 1
                if lvl > 200: 
                    return True
                
                newStack = []
                for (x, y) in stack: 
                    if (x, y) == (x_, y_):
                        return True
                    for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= r < 1e6 and 0 <= s < 1e6:
                            if (r, s) not in blocked and (r, s) not in seen: 
                                seen[(r, s)] = True
                                newStack.append((r, s))
                                
                stack = newStack
            
            return False
        
        blocked = {(r,s): True for (r, s) in blocked}
        
        return helper(*source, *target) and helper(*target, *source)
