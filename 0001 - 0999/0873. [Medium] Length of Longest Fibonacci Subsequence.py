# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(lambda: 2)
        
        seen = {num for num in arr}
        
        ans = 0 
        
        for (i, numA) in enumerate(arr):
            for numB in arr[: i]:
                numC = numA - numB
                
                if numC in seen and numC < numB: 
                    dp[(numB, numA)] = dp[(numC, numB)] + 1  
                    
                    ans = max(ans, dp[(numB, numA)])
                    
        return ans
                
                
            
