# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, i):
            if i == n: 
                ans.append(arr.copy())
                
            else: 
                for (j, num) in enumerate(nums): 
                    if not visited[j]:
                        visited[j] = True 
                        arr.append(num)
                        
                        helper(arr, i + 1)
                        
                        visited[j] = False
                        arr.pop() 
            
        n = len(nums)
        
        visited = [False for _ in range(n)]
        
        ans = []
        
        helper([], 0)
        
        return ans 
        
                    
            
        
        
        
        
