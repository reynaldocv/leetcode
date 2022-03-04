# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        prefix = [0]
        for num in nums: 
            prefix.append(prefix[-1] + num)
        
        ans = 0
        for i in range(1, len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            
            ans += max(0, min(len(nums), k) - max(i + 1, j))
            
        return ans % MOD
