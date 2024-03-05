# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        stack = ["0000"]
        seen = {"0000"}
        
        deadends = {elem for elem in deadends}
        
        ans = 0
        
        while stack: 
            newStack = []
            
            for elem in stack: 
                if elem == target: 
                    return ans 
                
                if elem not in deadends: 
                    for i in range(4):
                        newUp = elem[: i] + str((int(elem[i]) + 1) % 10) + elem[i + 1: ]

                        if newUp not in seen: 
                            seen.add(newUp)

                            newStack.append(newUp)

                        newDown = elem[: i] + str((int(elem[i]) - 1) % 10) + elem[i + 1: ]

                        if newDown not in seen: 
                            seen.add(newDown)

                            newStack.append(newDown)

            stack = newStack 
            ans += 1 
            
        return -1
            
            
            
            
                        
                    
                    
                    
                    
            
        
        
        
        
        
