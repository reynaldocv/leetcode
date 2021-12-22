# https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        
        if start.replace("X", "") != end.replace("X", ""):
            return False
    
        index1 = [i for (i, char) in enumerate(start) if char != "X"]
        index2 = [i for (i, char) in enumerate(end)   if char != "X"]
            
        for (i, char) in enumerate(start.replace("X", "")):
            if char == "R":
                if index1[i] > index2[i]:
                    return False 
            else: 
                if index1[i] < index2[i]:
                    return False
                
        return True
            
        
        
        
        
        
        
        

        
