# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def helper(value):
            ans = 0
            
            for workTime in workerTimes:
                tmp = 2*(value//workTime)
                
                sqrt = int(tmp**.5)
                
                if sqrt*(sqrt + 1) > tmp:
                    sqrt -=1
                    
                ans += sqrt
                
            return ans >= mountainHeight
            
        start = -1
        end = mountainHeight**2*min(workerTimes)
        
        while end - start > 1:
            mid = (end + start)//2
            
            if helper(mid) == True:
                end = mid 
                
            else:
                start = mid 
                
        return end 
