# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def isPalindromic(string):
            return string == string[::-1]
            
        def helper(start, arr):
            if start >= n: 
                ans.append(arr[:])
            else: 
                for i in range(start + 1, n + 1):
                    prefix = s[start: i]    
                    if isPalindromic(prefix):
                        arr.append(prefix)
                        helper(i, arr)
                        arr.pop()
                
        ans = []
        n = len(s)
        
        helper(0, [])
        
        return ans
