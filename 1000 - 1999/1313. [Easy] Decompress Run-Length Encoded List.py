# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        ans = []
        
        for i in range(n//2):
            freq = nums[2*i]
            val = nums[2*i + 1]
            
            for _ in range(freq):
                ans.append(val)
                
        return ans 
            
        
