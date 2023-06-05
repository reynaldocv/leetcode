# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, i):
            if i == n: 
                if tuple(arr) not in seen: 
                    seen.add(tuple(arr))
                    
                    ans.append(arr[: -1])
                
            else: 
                for j in range(i, n):
                    arr.append(nums[j])
                    
                    helper(arr, j + 1)
                    
                    arr.pop()
                    
        nums.sort()
        
        nums.append(inf)  
        
        n = len(nums) 
        
        ans = []
        
        seen = set()
        
        helper([], 0)
        
        return ans 
                
