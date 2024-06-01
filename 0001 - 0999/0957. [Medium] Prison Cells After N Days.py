# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def helper(prison): 
            ans = [0 for _ in range(8)]
            
            for i in range(1, 7):
                if prison[i - 1] == prison[i + 1]:
                    ans[i] = 1 
                    
            return tuple(ans)
        
        status = tuple(cells)
        
        indexs = {}
        tuples = {}
        
        ith = 0 
        
        while status not in indexs:
            indexs[status] = ith
            tuples[ith] = status
            
            ith +=1  
            
            status = helper(status) 
            
        idx = n 
        
        if  n not in tuples: 
            start = indexs[status]  
            cycle = ith - start
            
            idx = ((n - start) % cycle) + start
            
        return tuples[idx]
            
            
            
            
        
            
        
