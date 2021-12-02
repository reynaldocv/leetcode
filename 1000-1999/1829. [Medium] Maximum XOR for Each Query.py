# https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        
        val = 2**maximumBit - 1
        aux = 0
        for i in range(n):
            aux ^= nums[i]            
            ans[n - 1 - i] = aux ^ val
            
        return ans
            
            
        
