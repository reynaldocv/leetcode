# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def isPalindromic(string):
            return string == string[::-1]
            
        def helper(i, arr):
            if i >= n: 
                ans.append(arr.copy())
                
            else: 
                for j in range(i + 1, n + 1):
                    tmp = s[i: j]    
                    
                    if isPalindromic(tmp): 
                        arr.append(tmp)
                        
                        helper(j, arr)
                        
                        arr.pop()
                
        ans = []
        
        n = len(s)
        
        helper(0, [])
        
        return ans
        
