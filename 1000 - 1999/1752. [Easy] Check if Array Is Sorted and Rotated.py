# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:        
        A = [str(num) for num in nums]
        nums.sort()
        B = [str(num) for num in nums]
        
        A.extend(A)
        a = "-".join(A)
        b = "-".join(B)
        print(a,b)
        return b in a
        
