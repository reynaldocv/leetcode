# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        ans = [0, 0]
        
        for key in counter: 
            ans[0] += counter[key]//2
            ans[1] += counter[key] % 2
            
        return ans 
            
