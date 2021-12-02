# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(arr, i, aSum):
            if aSum == self.target: 
                self.ans.append(arr.copy())
            elif aSum < self.target: 
                for j in range(i, len(self.candidates)):
                    if self.counter[self.candidates[j]] > 0:                
                        self.counter[self.candidates[j]] -= 1                        
                        arr.append(self.candidates[j])
                        backtracking(arr, j, aSum  + self.candidates[j])
                        arr.pop()
                        self.counter[self.candidates[j]] += 1                        
        
        self.target = target 
        self.counter = {}
        for candidate in candidates: 
            self.counter[candidate] = self.counter.get(candidate, 0) + 1
        self.candidates = [*self.counter]
        self.ans = []
        backtracking([], 0, 0)
        
        return self.ans
            
