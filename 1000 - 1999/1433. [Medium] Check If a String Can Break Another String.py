# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def helper(letters1, letters2):
            for i in range(n):
                if letters2[i] < letters1[i]:
                    return False 

            return True 

        n = len(s1)

        arr1 = sorted(s1)
        arr2 = sorted(s2)
        
        return helper(arr1, arr2) or helper(arr2, arr1)
         
        
