# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        ans = 0 
        
        for key in counter: 
            ans += (counter[key] - 1)*counter[key]//2
            
        return ans 
        
