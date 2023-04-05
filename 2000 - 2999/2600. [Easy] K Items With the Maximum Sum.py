# https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes: 
            return k 
        
        ans = numOnes
        
        k -= numOnes
        
        if k <= numZeros: 
            return ans 
        
        else:
            k -= numZeros
        
            return ans - k
