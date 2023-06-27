# https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        tmp = 2**maximumBit - 1
        
        prev = 0 
        
        ans = []
        
        for num in nums: 
            prev ^= num 
            
            ans.append(prev^tmp)
            
        return ans[:: -1]
            
        
            
        
