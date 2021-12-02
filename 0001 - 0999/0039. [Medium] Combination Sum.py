# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def recursive(arr, i, aSum):
            if aSum == self.target: 
                self.ans.append(arr)
            elif aSum < self.target: 
                for j in range(i, len(self.candidates)):
                    arr2 = arr.copy()
                    arr2.append(self.candidates[j])
                    recursive(arr2, j, aSum  + self.candidates[j])
        
        self.target = target 
        self.candidates = candidates
        self.ans = []
        
        recursive([], 0, 0)
        
        return self.ans
