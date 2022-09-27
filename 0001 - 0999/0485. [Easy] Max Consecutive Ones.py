# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0 
        counter = 0 
        
        for num in nums + [0]:
            if num == 0: 
                ans = max(ans, counter)
                counter = 0 
                
            else: 
                counter += 1 
             
        return ans 
    
