# https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        maxFreq = 0 
        
        for num in nums: 
            counter[num] += 1 
            
            maxFreq = max(maxFreq, counter[num])
            
        ans = 0 
        
        for num in nums: 
            if counter[num] == maxFreq: 
                ans += 1 
                
        return ans 
        
