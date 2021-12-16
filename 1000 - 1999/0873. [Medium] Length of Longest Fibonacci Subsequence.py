# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = defaultdict(lambda: 2)
        index = {num: i for (i, num) in enumerate(arr)}
        
        ans = 0 
        
        for (i, numA) in enumerate(arr):
            for (j, numB) in enumerate(arr[:i]):
                idx = index.get(numA - numB, None)
                if idx != None and idx < j: 
                    aux = dp[(numB, numA)] = dp[(arr[idx], numB)] + 1
                    ans = max(ans, aux)
                    
        return ans
                    
                    
            
