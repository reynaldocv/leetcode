# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        index = defaultdict(lambda: -1)
        
        ans = 0 
        
        counter = 0 
        
        for (i, num) in enumerate(nums):
            if num == 0: 
                counter += 1 
                
                index[counter] = i 
                
            ans = max(ans, i - index[counter - k])            
                
        return ans 
        
