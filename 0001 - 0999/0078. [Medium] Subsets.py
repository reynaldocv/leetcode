# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums: 
            aux = []
            for subset in ans: 
                aux.append(subset + [num])
                
            ans.extend(aux)
            
        return ans

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(arr, i, n,  elems):
            if i <= n: 
                self.ans.append(list(arr))
                for j in range(i, n):
                    arr.append(elems[j])
                    backtracking(arr, j + 1, n, elems)
                    arr.pop()
        
        self.ans = []
        backtracking([], 0, len(nums), nums)
        
        return self.ans
                
        
        
        
