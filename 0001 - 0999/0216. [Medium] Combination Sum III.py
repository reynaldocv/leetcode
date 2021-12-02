# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def recursive(arr, k, minElem, n):
            if len(arr) == k: 
                if sum(arr) == n:
                    self.ans.append(list(arr))
            else:
                for j in range(minElem + 1, 10):
                    arr.append(j)
                    recursive(arr, k, j, n)
                    arr.pop()
                    
        self.ans = []
        recursive([], k, 0, n)
        
        return self.ans
                
class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        for comb in combinations([i for i in range(1, 10)], k):
            if sum(comb) == n:
                ans.append(list(comb))
                
        return ans
        
