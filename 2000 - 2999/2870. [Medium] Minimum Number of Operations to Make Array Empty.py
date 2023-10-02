# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        ans = 0 
        
        for key in counter: 
            if counter[key] <= 1: 
                return -1 
            
            else: 
                ans += ceil(counter[key]/3)
                
        return ans 
