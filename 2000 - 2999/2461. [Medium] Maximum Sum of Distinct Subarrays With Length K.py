# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        index = defaultdict(lambda: -1)
        prev = [0]
        
        last = -1 
                
        aSum = 0 
        
        ans = 0
    
        for (ith, num) in enumerate(nums):
            aSum += num 
            
            last = max(last, index[num])
            
            if ith + 1 >= k: 
                if ith + 1 - k > last:
                    ans = max(ans, aSum - prev[ith - k + 1])
                    
            index[num] = ith
            prev.append(prev[-1] + num)
        
        return ans 
        
