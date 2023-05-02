# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums) 
        
        prev = -1
        
        ans = []
        
        for i in range(n):
            if nums[i] == key: 
                for j in range(max(i - k, 0), min(n, i + k + 1)):
                    if prev < j: 
                        ans.append(j)
                        prev = j
                        
        return ans 
                
        
        
