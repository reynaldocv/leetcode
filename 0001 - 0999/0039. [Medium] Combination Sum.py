# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, idx):
            if sum(arr) == target: 
                ans.append(arr[: ])
                
            else: 
                for i in range(idx, n):
                    if sum(arr) + candidates[i] <= target: 
                        helper(arr + [candidates[i]], i)
                        
        n = len(candidates)
        
        ans = []
        
        helper([], 0)
        
        return ans 
            
        
