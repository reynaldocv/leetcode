# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = []
        for i in range(l//2):
            for j in range(nums[2*i]):
                ans.append(nums[2*i + 1])
        return ans
            
        
