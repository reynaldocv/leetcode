# https://leetcode.com/problems/xor-queries-of-a-subarray/submissions/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        accXor = [num for num in arr]
        
        for i in range(1, n):
            accXor[i] ^= accXor[i - 1]
        
        ans = []
        for [start, end] in queries: 
            aux = accXor[end]
            if start > 0: 
                aux ^= accXor[start - 1]
            ans.append(aux)
            
        return ans
            
        
        
