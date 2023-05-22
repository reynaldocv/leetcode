# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(arr):
            if len(arr) == n: 
                if tuple(arr) not in seen: 
                    seen.add(tuple(arr))
                    
                    ans.append(arr[: ])
                
            else: 
                for (i, num) in enumerate(nums):
                    if visited[i] == False:
                        arr.append(num)
                        visited[i] = True 
                        
                        helper(arr)
                        
                        arr.pop() 
                        visited[i] = False
                        
        n = len(nums)
        
        visited = [False for _ in range(n)]
        
        seen = set()
        
        ans = []
        
        helper([])
        
        return ans 
        
