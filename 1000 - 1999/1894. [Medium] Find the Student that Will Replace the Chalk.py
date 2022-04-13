# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        aSum = sum(chalk)
        k = k % aSum 
        
        for (i, val) in enumerate(chalk):
            if k < val: 
                return i
            else: 
                k -= val
                
class Solution2:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix = [0]
        
        for num in chalk: 
            prefix.append(prefix[-1] + num)
        
        k = k % prefix[-1]
        
        start = 0       
        end = len(prefix) - 1
        
        while end - start > 1: 
            mid = (end + start)//2
            if prefix[mid] < k: 
                start = mid
            else: 
                end = mid
                
        if prefix[end] == k: 
            end += 1 
       
        return end - 1
                 
        
        
