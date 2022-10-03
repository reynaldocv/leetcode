# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        ans = 0 
        
        for num in nums: 
            counter[num] += 1 
            
            if num + 1 in counter:             
                ans = max(ans, counter[num] + counter[num + 1])
                
            if num - 1 in counter: 
                ans = max(ans, counter[num] + counter[num - 1])
            
        return ans 
    
    
