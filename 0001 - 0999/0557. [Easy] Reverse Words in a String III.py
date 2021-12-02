# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ans = ""
        l = len(arr)
        for i in range(l - 1):
            ans += arr[i][::-1] + " "
        ans += arr[l - 1][::-1]
        return ans
        
            
        
