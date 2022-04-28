# https://leetcode.com/problems/find-a-peak-element-ii/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        
        low = -1
        high = m - 1 
        
        while high - low > 1:            
            mid = (high + low)//2
            if max(mat[mid]) >= max(mat[mid + 1]):
                high = mid
            else:
                low = mid
                
        return [high, mat[high].index(max(mat[high]))]
                
        
