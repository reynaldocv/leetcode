# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def helper(arr):        
            processing = False 
            ans = [inf for _ in range(n)]
            
            for (i, char) in enumerate(arr): 
                if char == ".":
                    if processing: 
                        ans[i] = ans[i - 1] + 1
                elif char == "R":
                    ans[i] = 1 
                    processing = True 
                else: 
                    processing = False
                    
            return ans
        
        n = len(dominoes)
        
        complement = {"R": "L", "L": "R", ".": "."}
        
        left = helper(dominoes)
        right = helper([complement[char] for char in dominoes][:: -1])[:: -1]
        
        ans = ""       
        
        for i in range(n):
            if left[i] == right[i]:
                ans += "."
            elif left[i] < right[i]:
                ans += "R"
            else: 
                ans += "L"
                
        return ans 
