# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def helper(val):
            ans = 0 
            cnt = 0 
            for num in bloomDay: 
                if num <= val: 
                    cnt += 1 
                    if cnt == k: 
                        ans += 1 
                        cnt = 0 
                else: 
                    cnt = 0 
            
            return ans 
            
        n = len(bloomDay)
        if m*k > n: 
            return -1
        
        elif m*k == n: 
            return max(bloomDay)
        
        start = 0 
        end = max(bloomDay)
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle) < m: 
                start = middle
            else: 
                end = middle
                
        return end 
        
        
        
