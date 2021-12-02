# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False for _ in range(n)]
        ans = 1
        for i in range(n):
            if visited[i] == False: 
                aux = 0
                while visited[i] == False:
                    visited[i] = True
                    i = nums[i]
                    aux += 1
                ans = max(ans, aux)
        
        return ans
        
