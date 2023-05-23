# https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(key = lambda item: -item)
        
        counter = defaultdict(lambda: 0)
        
        ans = -1
        
        for num in nums: 
            if num**2 in counter: 
                counter[num] = 1 + counter[num**2]
                
                ans = max(ans, counter[num])
                
            else: 
                counter[num] = 1
            
        return ans 
                
