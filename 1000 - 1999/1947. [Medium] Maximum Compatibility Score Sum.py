" https://leetcode.com/problems/maximum-compatibility-score-sum/

from itertools import permutations

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        def Hamming (a, b):
            ans = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    ans += 1
            return ans
        
        m = len(students)
        perm = permutations([i for i in range(m)])
        
        ans = 0
        for p1 in perm: 
            sum_ = 0                             
            for i in range(m): 
                sum_ += Hamming(students[i], mentors[p1[i]])
   
            ans = max(ans, sum_)
        return ans
                        
