# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:        
        i, j = 0, 0
        
        n = len(start)
        begin = -1
        
        while i < n or j < n: 
            while i < n and start[i] == "_":
                i += 1 
                
            char1 = start[i] if i < n else "_"
                
            while j < n and target[j] == "_":
                j += 1 
                
            char2 = target[j] if j < n else "_"
                
            if char1 != char2: 
                return False 
            
            else: 
                if char1 == "L":
                    if begin < j and j <= i: 
                        begin = j
                    else: 
                        return False 
                else: 
                    if begin < j and i <= j: 
                        begin = j 
                    else: 
                        return False 
            
            i += 1 
            j += 1 
                    
        return True 

class Solution2:
    def canChange(self, start: str, target: str) -> bool:        
        arr1 = [(i, char) for (i, char) in enumerate(start)]
        arr2 = [(i, char) for (i, char) in enumerate(target)]
        
        if len(arr1) != len(arr2):
            return False
        
        begin = -inf         
        for (i, (start1, char1)) in enumerate(arr1):             
            (start2, char2) = arr2[i]
            
            if char1 != char2: 
                return False             
            else:
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
                
            
            
            
        
        
        
