# https://leetcode.com/problems/combinations/

from itertools import permutations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(arr, k, i, elems, visited):
            if len(arr) == k: 
                self.ans.append(list(arr))              
            elif len(arr) < k:
                for j in range(i, len(elems)):
                    if visited[j] == False: 
                        arr.append(elems[j])
                        visited[j] = True
                        backtracking(arr, k, j + 1, elems, visited)
                        visited[j] = False
                        arr.pop()
        
        self.ans = []
        visited = [False for i in range(n)]
        elems = [i + 1 for i in range(n)]
        backtracking([], k, 0, elems, visited)
        
        return self.ans
                        
                
