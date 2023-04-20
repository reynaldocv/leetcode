# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr) 
        
        index = {}
        
        for (i, num) in enumerate(arr):
            index[num] = i 
            
        for piece in pieces: 
            m = len(piece)
            
            if piece[0] not in index: 
                return False 
            
            idx = index[piece[0]]
            
            for i in range(1, m):
                if idx + i < n and arr[idx + i] == piece[i]:
                    continue 
                    
                else: 
                    return False
                
        return True 
                    
