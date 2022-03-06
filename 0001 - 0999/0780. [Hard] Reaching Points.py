# https://leetcode.com/problems/reaching-points/

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx or sy < ty: 
            if tx > ty: 
                k = (tx - sx)//ty 
                if k == 0: 
                    break
                    
                tx -= k * ty
                
            else: 
                k = (ty - sy)//tx 
                if k == 0: 
                    break 
                    
                ty -= k * tx
                
        return sx == tx and sy == ty
        
