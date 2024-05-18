# https://leetcode.com/problems/largest-time-for-given-digits/

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        times = set()
        
        for h in range(24):
            for m in range(60):
                hours = str(h)
                
                if h < 10: 
                    hours = "0" + hours
                    
                minutes = str(m)
                
                if m < 10: 
                    minutes = "0" + minutes
                    
                time = hours + ":" + minutes
                
                times.add(time)
                
        ans = aux = chr(ord("0") - 1)
        
        for (a, b, c, d) in permutations(arr, 4):
            tmp = str(a) + str(b) + ":" + str(c) + str(d)
            
            if tmp in times:                 
                ans = max(ans, tmp)
                
        return "" if ans == aux else ans 
            
                
        
