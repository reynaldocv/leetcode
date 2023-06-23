# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        
        ans = [0 for _ in range(n)]
        
        lastA = {}
        lastB = {}
        
        for i in range(n):
            lastA[A[i]] = i 
            lastB[B[i]] = i
            
        for char in lastA: 
            maxIdx = max(lastA[char], lastB[char])
            
            ans[maxIdx] += 1 

        for i in range(n - 1):
            ans[i + 1] += ans[i]
            
        return ans 
