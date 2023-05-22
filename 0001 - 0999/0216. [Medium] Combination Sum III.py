# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(arr, last):
            if len(arr) == k: 
                if sum(arr) == n: 
                    ans.append(arr[: ])
                
            else: 
                for i in range(last, 10):
                    helper(arr + [i], i + 1)
                    
        ans = []
        
        helper([], 1)
        
        return ans 
                

