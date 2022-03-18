# https://leetcode.com/problems/cinema-seat-allocation/

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def helper(arr):
            val1, val2, val3 = 0, 0, 0
            for x in arr: 
                if 2 <= x <= 5:
                    val1 += 1 
                if 6 <= x <= 9:
                    val2 += 1
                if 4 <= x <= 7:
                    val3 += 1 
                    
            if val1 == 0 and val2 == 0:
                return 2
            elif val1 == 0 or val2 == 0 or val3 == 0:
                return 1
            else: 
                return 0
            
        reserved = defaultdict(lambda: [])
        for (row, col) in reservedSeats: 
            reserved[row].append(col)
        
        ans = (n - len(reserved))*2
        
        for key in reserved:
            ans += helper(reserved[key])
            
        return ans 
