# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        last = -1 
        index = defaultdict(lambda: defaultdict(lambda: -1))
        
        counter = defaultdict(lambda: 0)
        
        ans = 0 
        
        for (i, num) in enumerate(nums): 
            cnt = counter[num] + 1  
            
            last = max(last, index[num][cnt - k])
            
            ans = max(ans, i - last)
            
            counter[num] += 1 
            index[num][cnt] = i 
            
        return ans 
        
