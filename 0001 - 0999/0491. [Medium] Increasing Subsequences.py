# https://leetcode.com/problems/increasing-subsequences/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(seq, start):
            for i in range(start, n):
                if seq[-1] <= nums[i]:                    
                    tmp = seq + (nums[i], )
                    
                    if tmp not in ans:                     
                        ans.add(tmp)

                        helper(tmp, i + 1)

        n = len(nums)
        
        ans = set([])
        
        for (i, num) in enumerate(nums):
            helper((num, ), i + 1)
        
        return ans
                
                    
        
        
        
