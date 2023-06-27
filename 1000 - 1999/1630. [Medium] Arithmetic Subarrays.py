# https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def helper(arr):
            m = len(arr)
            
            ratio = tmp[0] - tmp[1]
                
            for i in range(m - 1):
                if arr[i] - arr[i + 1] != ratio:
                    return False 
                
            return True 
                                
        n = len(l) 
        
        ans = []
        
        for i in range(n):
            start = l[i]            
            end = r[i]
            
            tmp = nums[start: end + 1]            
            tmp.sort()
                
            ans.append(helper(tmp))
            
        return ans 
        
        
