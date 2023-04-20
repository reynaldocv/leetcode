# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def helper(arr, diff):        
            aSum = sum(arr[: diff])
            
            ans = []
            
            for i in range(n):
                aSum += arr[(i + diff) % n] - arr[i]
                
                ans.append(aSum)
                
            return ans 
        
        n = len(code)
        
        if k == 0: 
            return [0 for _ in range(n)]
        
        elif k > 0: 
            return helper(code, k)
        
        else: 
            return helper(code[:: -1], -k)[:: -1]
                
            
        
        
