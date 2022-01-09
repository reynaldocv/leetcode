# https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(lambda: 0)
        seen[0] += 1
        ans = 0
        prev = 0 
        for (i, num) in enumerate(nums):
            prev = (prev + num) % k
            
            if prev in seen: 
                ans += seen[prev]
                
            seen[prev] += 1
        
        return ans
            
