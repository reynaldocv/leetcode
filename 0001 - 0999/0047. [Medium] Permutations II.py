# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutations(arr, elems, visited, n, exist):
            if len(arr) == n: 
                aux = [str(ar) for ar in arr]               
                key = "-".join(aux)
                if key not in exist: 
                    self.ans.append(list(arr))
                    exist[key] = True
            else:
                for i in range(n): 
                    if visited[i] == False: 
                        visited[i] = True
                        arr.append(elems[i])
                        permutations(arr, elems, visited, n, exist)
                        arr.pop()
                        visited[i] = False
        
        visited = [False for num in nums]
        exist = {}
        n = len(nums)
        self.ans = []
        permutations([], nums, visited, n, exist)
        
        return self.ans
