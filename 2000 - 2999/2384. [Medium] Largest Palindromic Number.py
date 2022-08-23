# https://leetcode.com/problems/largest-palindromic-number/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in num: 
            counter[char] += 1
        
        ans = ""
        maxElem = ""
        
        for num in range(9, -1, -1):
            val = str(num)
            if val == "0":
                if ans != "":
                    ans += val*(counter[val]//2)
            else: 
                ans += val*(counter[val]//2)
                
            if counter[val] % 2 == 1 and maxElem == "": 
                maxElem = val
                
        ans = ans + maxElem + ans[:: -1]
        
        return "0" if ans == "" else ans 
