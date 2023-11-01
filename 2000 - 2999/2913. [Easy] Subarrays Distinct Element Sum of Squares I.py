# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            counter = defaultdict(lambda: 0)
            
            for j in range(i, n):
                counter[nums[j]] += 1 
                
                ans += len(counter)**2
                
        return ans 
            
        
