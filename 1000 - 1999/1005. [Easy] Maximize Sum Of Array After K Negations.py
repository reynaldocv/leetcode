# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg, pos = [], []
        for num in nums: 
            if num < 0: 
                neg.append(num)
            else: 
                pos.append(num)
        n = len(pos)
        m = len(neg)
        pos.sort()
        neg.sort()
     
        if m == 0: 
            if k % 2 == 1 and 0 not in pos: 
                pos[0] *= -1
        elif k <= m: 
            for i in range(k):
                neg[i] *= -1
        else: 
            for i in range(m):
                neg[i] *= -1
            k -= m
            pos.extend(neg)
            pos.sort()
            neg = []
            if 0 not in pos and k % 2 == 1: 
                pos[0] *= -1 
                
        print(pos, neg)
        return sum(pos) + sum(neg)
