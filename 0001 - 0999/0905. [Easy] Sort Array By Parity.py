# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans1 = []
        ans2 = [] 
        l = len(A)
        for i in range(l):
            if A[i] % 2 == 0: 
                ans1.append(A[i])
            else:
                ans2.append(A[i])
        return ans1 + ans2
            
            
                
