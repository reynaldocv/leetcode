# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(j//2 + 1):
            s[i], s[j] = s[j], s[i]
            j -= 1
