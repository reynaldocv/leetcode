# https://leetcode.com/problems/increasing-subsequences/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)        
        ans = set()
        for (i, num) in enumerate(nums): 
            aux = set()
            
            for seq in ans: 
                if seq[-1] <= num: 
                    aux.add(seq + (num,))
            
            for j in range(i):                
                if nums[j] <= num: 
                    aux.add((nums[j], num))
            
            for seq in aux: 
                ans.add(seq)
                    
        return ans
                
                    
        
        
        
