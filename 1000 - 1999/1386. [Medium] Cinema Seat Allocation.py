# https://leetcode.com/problems/cinema-seat-allocation/

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def helper(occupied):
            if all(i not in occupied for i in range(2, 10)) == True:
                return 2 
            
            elif all(i not in occupied for i in range(2, 6)) == True:
                return 1
        
            elif all(i not in occupied for i in range(6, 10)) == True:
                return 1
            
            elif all(i not in occupied for i in range(4, 8)) == True:
                return 1
            
            else: 
                return 0 
            
        reservedSeats.sort() 
        
        reserved = set()
        prev = 0
        
        rows = set()
        
        ans = 0 
        
        for (row, seat) in reservedSeats: 
            if row != prev: 
                if len(reserved) > 0: 
                    ans += helper(reserved)
                    
                reserved = {seat}
                
            else: 
                reserved.add(seat)
                
            prev = row
            rows.add(row)
        
        ans += helper(reserved) + 2*(n - len(rows))
                
        return ans 
            
            
