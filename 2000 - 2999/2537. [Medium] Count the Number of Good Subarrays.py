# https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        prev = 0 
        
        start = 0 
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            counter[num] += 1 
            
            prev += counter[num] - 1 
            
            while start <= i and prev >= k: 
                ans += n - i 
                
                number = nums[start]
                
                counter[number] -= 1 
                
                prev -= counter[number]
                    
                start += 1 
                    
        return ans 
