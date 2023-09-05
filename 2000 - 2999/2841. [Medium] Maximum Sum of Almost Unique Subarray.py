# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        
        if n < k: 
            return 0 
        
        left = 0 
        counter = defaultdict(lambda: 0)
        
        for num in nums[: k - 1]:
            left += num             
            counter[num] += 1 
            
        ans = 0 
        
        for (i, num) in enumerate(nums[k - 1: ]):
            left += num            
            counter[num] += 1
            
            if len(counter) >= m: 
                ans = max(ans, left)
                
            old = nums[i]
            
            counter[old] -= 1 
            left -= old

            if counter[old] == 0: 
                counter.pop(old)
                
        return ans 
            
