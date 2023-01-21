# https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        minimum = defaultdict(lambda: -1)
        
        tmp = (-inf, -inf)
        
        counter = defaultdict(lambda: 0)
        
        for (i, num) in enumerate(nums): 
            if minimum[num] == -1:
                minimum[num] = i 
            
            counter[num] += 1 
            
            tmp = max(tmp, (counter[num], -(i - minimum[num] + 1)))
                
        return -tmp[1]
            
        
            
            
            
        
        
