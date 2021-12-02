# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(arr, elems, visited, n):
            if len(arr) == n: 
                self.ans.append(list(arr))
            else: 
                for i in range(n):
                    if visited[i] == False: 
                        visited[i] = True
                        arr. append(elems[i])
                        permutations(arr, elems, visited, n)
                        arr.pop()
                        visited[i] = False
            
        visited = [False for num in nums]
        n = len(nums)
        self.ans = []
        permutations([], nums, visited, n)
        
        return self.ans
                    
            
        
        
        
        
