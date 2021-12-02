# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(arr, elems, i, n, key, visited):
            if key not in visited: 
                self.ans.append(arr.copy())
                visited[key] = True
                for j in range(i, n):
                    if counter[elems[j]] > 0:
                        counter[elems[j]] -= 1
                        arr.append(elems[j])
                        backtracking(arr, elems, j, n, key + "-" + str(elems[j]), visited)
                        arr.pop()
                        counter[elems[j]] += 1
                        
        counter = {}
        for num in nums: 
            counter[num] = counter.get(num, 0) + 1            
        elems = [*counter]
        elems.sort()
        visited = {}        
        self.ans = []
    
        backtracking([], elems, 0, len(elems), "", visited)
        
        return self.ans
