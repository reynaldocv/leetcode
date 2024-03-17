# https://leetcode.com/problems/largest-palindromic-number/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in num: 
            counter[char] += 1 
            
        border = ""
        center = ""
        
        for char in "9876543210":
            border += char*(counter[char]//2)

            if counter[char] % 2 == 1: 
                center = max(center, char)

        while border and border[0] == "0":
            border = border[1: ]
            
        ans = border + center + border[:: -1]
        
        if ans == "":
            return "0"
        
        else: 
            return ans 
