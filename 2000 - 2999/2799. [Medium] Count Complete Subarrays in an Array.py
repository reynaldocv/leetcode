# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len({num for num in nums})
        
        counter = defaultdict(lambda: 0) 
        
        ans = start = 0
        
        for num in nums: 
            counter[num] += 1 
            
            while len(counter) == m: 
                if counter[nums[start]] > 1: 
                    counter[nums[start]] -= 1
                    
                    start += 1 
                    
                else: 
                    break 
                    
            if len(counter) == m: 
                ans += start + 1
                
        return ans 
                    
                
            
            
        
