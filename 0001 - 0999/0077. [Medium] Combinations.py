# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(arr, idx, cnt):
            if cnt == 0: 
                ans.append(arr[: ])
                
            else: 
                for j in range(idx, n):                    
                    arr.append(nums[j]) 
                    
                    helper(arr, j + 1, cnt - 1)
                    
                    arr.pop() 
                    
        nums = [i for i in range(1, n + 1)] 
        
        ans = []
        
        helper([], 0, k)
        
        return ans 
        
                        
                
