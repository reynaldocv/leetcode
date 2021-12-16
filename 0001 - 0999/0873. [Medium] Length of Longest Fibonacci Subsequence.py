# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(lambda: 2)
        seen = {num: i for (i, num) in enumerate(arr)}
        
        ans = 0 
        
        for (i, numA) in enumerate(arr):
            for (j, numB) in enumerate(arr[:i]):
                numC = numA - numB
                if numC in seen and numC < numB: 
                    aux = dp[(numB, numA)] = dp[(numC, numB)] + 1                
                    ans = max(ans, aux)
                    
        return ans
                
        
                    
                    
            
