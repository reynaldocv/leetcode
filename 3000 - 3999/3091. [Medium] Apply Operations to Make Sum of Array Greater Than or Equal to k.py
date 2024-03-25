# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/submissions/

class Solution:
    def minOperations(self, k: int) -> int:
        def helper(number):
            quo = k//number 
            
            if quo*number != k: 
                quo += 1 
                
            return number - 1 + quo - 1
                
        root = int(k**.5)
        
        return min(helper(root), helper(root + 1))
        
        
