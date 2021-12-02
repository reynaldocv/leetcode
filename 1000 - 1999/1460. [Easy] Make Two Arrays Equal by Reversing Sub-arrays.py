# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        l, m = len(target), len(arr)
        if l != m:
            return False
        for i in range(l):
            if target[i] != arr[i]:
                return False
        return True
        
