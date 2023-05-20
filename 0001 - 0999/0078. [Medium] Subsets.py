# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        for num in nums: 
            tmp = []
            
            for arr in ans: 
                tmp.append(arr + [num])
                
            ans.extend(tmp)
            
        return ans 

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, i):
            if i == n: 
                ans.append(arr[: -1])
                
            else: 
                for j in range(i, n):
                    arr.append(nums[j])
                    
                    helper(arr, j + 1)
                    
                    arr.pop()
             
        nums.append(inf)
        
        n = len(nums)
        
        ans = []
        
        helper([], 0)
        
        return ans 
                
        
        
        
