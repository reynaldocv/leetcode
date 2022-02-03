# https://leetcode.com/problems/building-boxes/

class Solution:
    def minimumBoxes(self, n: int) -> int:
        start = 0 
        end = 10**9
        
        while end - start > 1: 
            m = (end + start)//2
            if m*(m + 1)*(m + 2)//6 <= n: 
                start = m
            else:
                end = m

        ans = start*(start + 1)//2
        n -= start*(start + 1)*(start + 2)//6
        
        if n > 0:             
            start = 0
            end = n            
            while end - start > 1: 
                m = (end + start)//2
                if m*(m + 1)//2 <= n: 
                    start = m
                else:
                    end = m

            ans += start 
            
            if start*(start + 1)//2 < n: 
                ans += 1 
                
        return ans
