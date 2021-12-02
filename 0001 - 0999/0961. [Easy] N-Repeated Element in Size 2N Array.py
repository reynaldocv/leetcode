# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = {}
        l = len(A)
        for i in range(l):
            counter[A[i]] = counter.get(A[i], 0) + 1
            if counter[A[i]] > 1:
                return A[i]
        
