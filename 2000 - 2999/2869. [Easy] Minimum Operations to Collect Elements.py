# https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        
        for (i, num) in enumerate(nums[:: -1]):
            if 1 <= num <= k: 
                seen.add(num)
                
                if len(seen) == k: 
                    return i + 1
                
        
        return -1 
                
