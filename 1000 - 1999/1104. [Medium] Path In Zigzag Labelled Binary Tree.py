# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        lvl = int(log(int(label), 2))
        
        last = label
        
        if lvl % 2 == 1: 
            last = 2**lvl + (2**(lvl + 1) - 1 - label)
            
        ans = []
        
        while lvl > 0: 
            value = last 
            
            if lvl % 2 == 1: 
                value = 2**lvl + (2**(lvl + 1) - 1 - last)
                
            ans.insert(0, value)    
            
            last //= 2                
            lvl -= 1 
            
        ans.insert(0, 1)
            
        return ans 
                
                
        
        
            
         
