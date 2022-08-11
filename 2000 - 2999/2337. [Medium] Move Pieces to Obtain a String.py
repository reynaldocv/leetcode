# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:        
        arr1 = []
        for (i, char) in enumerate(start):
            if char != "_":
                arr1.append((i, char))
                
        arr2 = []        
        for (i, char) in enumerate(target):
            if char != "_":
                arr2.append((i, char))
        
        if len(arr1) != len(arr2):
            return False
        
        begin = -inf         
        for (i, (start1, char1)) in enumerate(arr1):             
            (start2, char2) = arr2[i]
            
            if char1 != char2: 
                return False             
            else:
                print(char1, begin, start1, start2)
                if char1 == "L":
                    if begin < start2 and start2 <= start1: 
                        begin = start2
                    else: 
                        return False
                else: 
                    if begin < start2 and start1 <= start2: 
                        begin = start2
                    else: 
                        return False 
                    
        return True 
                
            
            
            
        
        
        
